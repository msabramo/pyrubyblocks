class EvalBlock(object):

    def __init__(self, code_string):
        self.code_object = compile(code_string, '<code>', mode='eval')

    def __call__(self, *args, **kwargs):
        return eval(self.code_object)


class ExecBlock(object):

    def __init__(self, code_string):
        self.code_object = compile(code_string, '<code>', mode='exec')

    def __call__(self, *args, **kwargs):
        return eval(self.code_object)


# Because we can't add methods to int in Python
class NumberObject(int):

    def times(self, block):
        for i in range(0, int(self)):
            block(i)

    def upto(self, upper_num, block):
        for i in range(int(self), int(upper_num)):
            block(i)


# Because we can't add methods to list in Python
class ListObject(list):

    def each(self, block):
        for item in self:
            block(item)

    def collect(self, block):
        return [block(item) for item in self]

    def select(self, block):
        return [item for item in self if block(item)]

    def reject(self, block):
        return [item for item in self if not block(item)]


NumberObject(5).times(ExecBlock("""
print "%d - %s" % (args[0], args[0] * '*')
"""))

NumberObject(1).upto(5, ExecBlock("""
print "%d - %s" % (args[0], args[0] * '*')
"""))

ListObject([1, 2, 3, 4]).each(ExecBlock("print args[0]"))

ret = ListObject([1, 2, 3, 4]).collect(EvalBlock("args[0] ** 2"))

print "result of collect => %r" % ret

ret = ListObject([1, 2, 3, 4, 5, 6, 7, 8, 9]).select(EvalBlock("args[0] %2 == 0"))

print "result of select => %r" % ret

ret = ListObject([1, 2, 3, 4, 5, 6, 7, 8, 9]).reject(EvalBlock("args[0] %2 == 0"))

print "result of reject => %r" % ret
