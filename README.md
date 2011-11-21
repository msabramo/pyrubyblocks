An experiment with emulating Ruby-style blocks in Python.

Some examples:

    ListObject([1, 2, 3, 4]).each(ExecBlock("print args[0]"))

    ret = ListObject([1, 2, 3, 4]).collect(EvalBlock("args[0] ** 2"))

    ret = ListObject([1, 2, 3, 4, 5, 6, 7, 8, 9]).select(EvalBlock("args[0] %2 == 0"))

    ret = ListObject([1, 2, 3, 4, 5, 6, 7, 8, 9]).reject(EvalBlock("args[0] %2 == 0"))
