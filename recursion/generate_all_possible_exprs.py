
def evaluate(val_1, val_2, optr):
    if optr == '""':
        return int(str(val_1) + str(val_2))
    if optr == "*":
        return int(val_1) * int(val_2)
    if optr == "+":
        return int(val_1) + int(val_2)

def preced(optr):
    if optr == '""':
        return -1
    if optr == "*":
        return -2
    if optr == "+":
        return -3

    
def sy_simple(expr):
    """
       Algorithm to compute expressions in a single pass
       Dijkstra's Shunting Yard, simplified:
       http://wcipeg.com/wiki/Shunting_yard_algorithm
       -Keep track of 2 stacks. 1. operators, 2. operands
       -Process expression from left to right following the rules below
         -1. before adding an operator, pop off all operators 
         on stack, of equal or higher precedence.(<-- only valid for 
         left accociative operators)
         Compute intermediate results as you go.
         -2. On reaching end, pop off all operators on stack and compute 
             final result.
       Operators with precedence, associativity,
       and arity ( wether operator is binary/varidac ):
       ------------------------------------------
       NO |  OPTOR  | ASSOC  |  PRECD  | ARITY  |
       ------------------------------------------
       1  |  ""     |  lt    |  1      |  2     |
       2  |   *     |  lt    |  2      |  2     |
       3  |   +     |  lt    |  3      |  2     |
       ------------------------------------------

       Notes: Parenthesis, right associative ^, varidac --> TBD
              Unary- is folded into expr
              Unary- at start of expr --> TBD
    """

    #print("Exrp: " + str(expr))
    
    #init stacks to first 3 tokens
    val_stk = [int(expr[0]), int(expr[2])]
    optr_stk = [expr[1]]
    
    def reduce_stk():
        val_2 = val_stk.pop()
        val_1 = val_stk.pop()
        optr = optr_stk.pop()
        val_stk.append(evaluate(val_1, val_2, optr))
        
    idx = 3
    while idx < len(expr) - 1:        
        while optr_stk and preced(expr[idx]) <= preced(optr_stk[-1]):
            reduce_stk()
              
        optr_stk.append(expr[idx])
        idx += 1
        val_stk.append(int(expr[idx]))
        idx += 1

    while optr_stk :
        reduce_stk()
    return val_stk[0]
                             
              
def generate_all_exprs(num, target):
    """
    Generate all exprs that evaluate to target value.
    """

    if not num:
        return []

    output = []

    def _dfs(partial_expr, idx):
        """
        Generate all permutaions of length --> 2n -1, where n is len(num)
        And add valid ones to output
        """
        if idx == len(num):
            if sy_simple(partial_expr) == target:
                output.append(partial_expr)
            return

        if idx == 0:
            _dfs([num[0]], idx + 1)

        else:
            _dfs(partial_expr + ['""', num[idx]], idx + 1)
            _dfs(partial_expr + ['*', num[idx]], idx + 1)
            _dfs(partial_expr + ['+', num[idx]], idx + 1)

        return


    _dfs([], 0)

    return output

print(generate_all_exprs('1234', 24))
         

        
    
