import argparse
import copy
from distutils.log import error
import random
from pyggi.base import Patch, AbstractProgram
#-- Epsilon Greedy
from greedy import ExpProtocol, MyAlgorithm, MyProgram, MySrcmlEngines, MyTreeProgram

from moea import MoeaNsgaProgram
from optipng import OptipngProgram

# ================================================================================
# Main function
# ================================================================================

if __name__ == "__main__":
    # setup protocol
    protocol = ExpProtocol()
    protocol.nb_epoch = 1
    protocol.search = MyAlgorithm() #validtest 
    #protocol.search.debug_patch = #
    protocol.search.stop['steps'] = 300
    protocol.program = OptipngProgram('./optipng-0.7.7') #call to moead

    # run experiments
    protocol.run()
    # ob = gra()
