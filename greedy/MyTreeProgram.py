import argparse
import copy
from distutils.log import error
import random
import numpy as np
import matplotlib.pyplot as plt
from pyggi.tree import StmtReplacement, StmtInsertion, StmtDeletion
from .MyProgram import MyProgram
from mutations import MultilineStatementDeletion, MultilineStatementReplacement, MultilineStatementInsertion
from mutations import expressionStatementDeletion, expressionStatementInsertion, expressionStatementReplacement
from mutations import declarationsStatementDeletion, declarationsStatementInsertion, declarationsStatementReplacement
from .MySrcmlEngines import MySrcmlEngines
import numpy as np
import time

class MyTreeProgram(MyProgram):
    def setup(self, config):
        self.target_files = ["Triangle.java.xml"]
        self.test_command = "./run.sh"
        self.possible_edits = [StmtReplacement, StmtInsertion, StmtDeletion, MultilineStatementDeletion, MultilineStatementInsertion, MultilineStatementReplacement, declarationsStatementDeletion, declarationsStatementInsertion,declarationsStatementReplacement, expressionStatementDeletion,expressionStatementInsertion,expressionStatementReplacement]

        self.rewards = {StmtReplacement:0.66, StmtInsertion:0.66, StmtDeletion:0.66, MultilineStatementDeletion:0.66, MultilineStatementInsertion:0.66, MultilineStatementReplacement:0.66, declarationsStatementDeletion:0.66, declarationsStatementInsertion:0.66,declarationsStatementReplacement:0.66, expressionStatementDeletion:0.66,expressionStatementInsertion:0.66,expressionStatementReplacement:0.66}

        self.last_edit_type = None

    @classmethod
    def get_engine(cls, file_name):
        return MySrcmlEngines

    def with_misc(self, result, start):
        result.walltime = round(time.time() - start, 3)
        result.budget = result.runtime_compile + result.runtime
        if result.fitness is not None:
            if self.base_fitness is None:
                self.base_fitness = result.fitness
                result.percentage = round(100.0, 2)
            else:
                result.percentage = round(100*result.fitness/self.base_fitness, 2)
        result.runtime_compile = round(result.runtime_compile, 3)
        result.runtime = round(result.runtime, 3)
        return result
        
    def debug_exec(self, cmd, status, return_code, stdout, stderr, elapsed_time):
        self.logger.debug('CMD: %s', repr(cmd))
        self.logger.debug('STATUS: %s', str(status))
        self.logger.debug('CODE: %s', str(return_code))
        self.logger.debug('STDOUT: %s', str(stdout))
        self.logger.debug('STDERR: %s', str(stderr))
        self.logger.debug('TIME: %s', str(elapsed_time))