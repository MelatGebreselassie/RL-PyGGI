from pyggi.tree.edits import NodeDeletion, NodeInsertion, NodeReplacement 



class MultilineStatementDeletion(NodeDeletion):
    NODE_TYPE = "multiline_stmt"

class MultilineStatementInsertion(NodeInsertion):
    NODE_PARENT_TYPE = 'block'
    NODE_TYPE = "multiline_stmt"

class MultilineStatementReplacement(NodeReplacement):
    NODE_TYPE = "multiline_stmt"


class declarationsStatementDeletion(NodeDeletion):
     
    NODE_TYPE = "declarations"

class declarationsStatementInsertion(NodeInsertion):
    NODE_PARENT_TYPE = 'block'
    NODE_TYPE = "declarations"

class declarationsStatementReplacement(NodeReplacement):
    NODE_TYPE = "declarations"


class expressionStatementDeletion(NodeDeletion):
    NODE_TYPE = "expression"

class expressionStatementInsertion(NodeInsertion):
    NODE_PARENT_TYPE = 'block'
    NODE_TYPE = "expression"

class expressionStatementReplacement(NodeReplacement):
    NODE_TYPE = "expression"


