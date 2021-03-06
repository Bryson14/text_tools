from Usage import usage


def cat(args):
    print("")
    try:
        for file in args:
            with open(file) as my_file:
                data = my_file.readlines()
                for line in data:
                        print(line[:-1 or None])
    except FileNotFoundError:
        usage("\n    Given file not found.", "cat")


def tac(args):
    print("")
    try:
        for file in args:
            with open(file) as my_file:
                data = my_file.readlines()
                for i in reversed(range(len(data))):
                    line = data[i]
                    print(line[:-1 or None])
    except FileNotFoundError:
        usage("\n    Given file not found.", "tac")

