import argparse
import copy
from distutils.log import error
import random
import numpy as np
import matplotlib.pyplot as plt
from pyggi.base import Patch, AbstractProgram
from pyggi.line import LineProgram
from pyggi.line import LineReplacement, LineInsertion, LineDeletion
from pyggi.tree.edits import NodeDeletion, NodeInsertion, NodeReplacement 
from pyggi.tree import SrcmlEngine
from pyggi.tree import StmtReplacement, StmtInsertion, StmtDeletion
from pyggi.algo import FirstImprovement
# import numpy as np
# stmtdel, stmtrep, stmtins, muldel,mulins, muldel, decrep, decdel, decins, expdel, exprep, expins = []
reward_list = []
graph_dict = {}
class MyAlgorithm(FirstImprovement):
   
    def hook_evaluation(self, patch, run, accept, best):
        super().hook_evaluation(patch, run, accept, best)
        if(self.program.last_edit_type is not None):
            reward = 0
            if (run.status == "SUCCESS"):
                # reward = 2 - run.fitness / self.program.base_fitness #
                reward = self.program.base_fitness / (self.program.base_fitness+run.fitness)
            self.rewards(self.program.last_edit_type, reward)
        self.program.last_edit_type = None
        self.program.logger.info('log file')
        print(run)
        

    def rewards(self, operator, reward):
        print("reward before", self.program.rewards[operator])
        # print("printting the keys", self.program.rewards.keys())
        # print("reward checking", self.program.rewards)
        alpha = 0.5 #ref: Mansour et al.
        self.program.rewards[operator] = self.program.rewards[operator] + alpha* (reward - self.program.rewards[operator])
        print("reward after", self.program.rewards[operator])
        reward_list.append(self.program.rewards)
    

        print("size of the reward list", len(reward_list))
    


# -----------GRAPHING THE REWARD---------

        
        k = 0
        for i in (self.program.rewards.keys()):
            # print("type of key", type(i))
            s = str(i)
            mutationText = s.split('.')[-1]
            k +=1
            if (len(graph_dict.keys())!=12):
                    graph_dict[mutationText]=[self.program.rewards[i]]
                    # print("we are here!",len(graph_dict.keys()) )
                    # print("type of key", type(graph_dict.keys()))
                    # print("type of key", type(graph_dict.keys()))
                    # print
            else:
                graph_dict[mutationText].append(self.program.rewards[i])

        # print("this is graph dict", graph_dict)

        if (len(reward_list)==1000 ):
            for f in (graph_dict.keys()):
                y = graph_dict.get(f)
                print('this is y', y)
                yaxis= len(y) + 1
                x = list(range(1, yaxis))
                print('this is x', x)
                # plot lines
                plt.plot(x, y, label = f)
                plt.xlabel('Steps')
                plt.ylabel('Rewards')
                plt.title('Reward graph over 300 steps')
                # name = "reward" + 
                from datetime import datetime
                plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
            date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
            plt.savefig(f"reward_{date}.png", bbox_inches='tight')
        