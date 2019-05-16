"""
Improving non-functional properties ::

    python improve_python.py ../sample/Triangle_fast_python
"""
import sys
import random
import argparse
from pyggi.base import Patch, ParseError, AbstractProgram
from pyggi.line import LineProgram
from pyggi.line import LineReplacement, LineInsertion, LineDeletion
from pyggi.tree import TreeProgram
from pyggi.tree import StmtReplacement, StmtInsertion, StmtDeletion
from pyggi.algorithms import LocalSearch

class MyProgram(AbstractProgram):
    def compute_fitness(self, elapsed_time, stdout, stderr):
        import re
        m = re.findall("runtime: ([0-9.]+)", stdout)
        if len(m) > 0:
            runtime = m[0]
            failed = re.findall("([0-9]+) failed", stdout)
            pass_all = len(failed) == 0
            if pass_all:
                return round(float(runtime), 3)
            else:
                raise ParseError
        else:
            raise ParseError

class MyLineProgram(LineProgram, MyProgram):
    pass

class MyTreeProgram(TreeProgram, MyProgram):
    pass

class MyLocalSearch(LocalSearch):
    def get_neighbour(self, patch):
        if len(patch) > 0 and random.random() < 0.5:
            patch.remove(random.randrange(0, len(patch)))
        else:
            edit_operator = random.choice(operators)
            patch.add(edit_operator.create(program))
        return patch

    def stopping_criterion(self, iter, fitness):
        return fitness < 0.05

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='PYGGI Improvement Example')
    parser.add_argument('--project_path', type=str, default='../sample/Triangle_fast_python')
    parser.add_argument('--mode', type=str, default='line')
    parser.add_argument('--epoch', type=int, default=30,
        help='total epoch(default: 30)')
    parser.add_argument('--iter', type=int, default=100,
        help='total iterations per epoch(default: 100)')
    args = parser.parse_args()
    assert args.mode in ['line', 'tree']

    if args.mode == 'line':
        program = MyLineProgram(args.project_path)
        operators = [LineReplacement, LineInsertion, LineDeletion]
    elif args.mode == 'tree':
        program = MyTreeProgram(args.project_path)
        operators = [StmtReplacement, StmtInsertion, StmtDeletion]

    local_search = MyLocalSearch(program)
    result = local_search.run(warmup_reps=5, epoch=args.epoch, max_iter=args.iter, timeout=15)
    print("======================RESULT======================")
    print(result)
    program.remove_tmp_variant()