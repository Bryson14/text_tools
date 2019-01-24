from Usage import usage


def grep(args):

    if args[0] == '-v':
        exclude(args[1:])
    else:
        include(args)


def include(args):
    print("")
    pass


def exclude(args):
    print("")
    pass
