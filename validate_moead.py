import argparse
import copy
from distutils.log import error
import random
from pyggi.base import Patch, AbstractProgram
#-- Epsilon Greedy
from greedy import ExpProtocol, MyAlgorithm, MyProgram, MySrcmlEngines, MyTreeProgram
from pyggi.tree import StmtReplacement, StmtInsertion, StmtDeletion
from mutations import MultilineStatementDeletion, MultilineStatementReplacement, MultilineStatementInsertion
from mutations import expressionStatementDeletion, expressionStatementInsertion, expressionStatementReplacement
from mutations import declarationsStatementDeletion, declarationsStatementInsertion, declarationsStatementReplacement

from moea import MoeaNsgaProgram
from pyggi.algo import ValidTest

# ================================================================================
# Main function
# ================================================================================

if __name__ == "__main__":
    # setup protocol
    protocol = ExpProtocol()
    protocol.nb_epoch = 1
    
    protocol.search = ValidTest()
    protocol.search.debug_patch = Patch([StmtReplacement(('DMOEA/dmoeafunc.h.xml', 'stmt', 0), ('DMOEA/dmoeafunc.h.xml', 'stmt', 1))])
    protocol.search.stop['steps'] = 1500
    protocol.program = MoeaNsgaProgram('./moead-2007') #call to moead

    # run experiments
    protocol.run()
    # ob = gra()
