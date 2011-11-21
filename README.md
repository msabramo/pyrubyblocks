An experiment with emulating Ruby-style blocks in Python.

Some examples:

    >>> ListObject([1, 2, 3, 4]).each(ExecBlock("print args[0]"))
    1
    2
    3
    4
    
    >>> ListObject([1, 2, 3, 4]).collect(EvalBlock("args[0] ** 2"))
    [1, 4, 9, 16]
    
    >>> ListObject([1, 2, 3, 4, 5, 6, 7, 8, 9]).select(EvalBlock("args[0] %2 == 0"))
    [2, 4, 6, 8]
    
    >>> ListObject([1, 2, 3, 4, 5, 6, 7, 8, 9]).reject(EvalBlock("args[0] %2 == 0"))
    [1, 3, 5, 7, 9]
