from pyrubyblocks import NumberObject, ExecBlock


def test_times():
    NumberObject(5).times(ExecBlock("""print "%d - %s" % (args[0], args[0] * '*')"""))

def test_upto():
    NumberObject(1).upto(5, ExecBlock("""print "%d - %s" % (args[0], args[0] * '*')"""))
