from pyggi.tree import SrcmlEngine


class MySrcmlEngines(SrcmlEngine):
    TAG_RENAME = {
            'stmt': {'break', 'continue', 'return', 'goto'},

            'multiline_stmt': {'do', 'for', 'if', 'switch', 'while'},

            'declarations': {'decl_stmt'},

            'expression': {'expr_stmt'}
            
        }

    TAG_FOCUS = {'block', 'stmt', 'multiline_stmt', 'declarations', 'expression'}


    PROCESS_LITERALS = False
    PROCESS_OPERATORS = False