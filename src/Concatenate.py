def cat(args):
    try:
        for file in args:
            with open(file) as myfile:
                print(myfile.readlines())
    except FileNotFoundError:
        print("Given file not found.")


def tac(args):
    try:
        for file in args:
            with open(file) as myfile:
                print(myfile.readlines(-1))
    except FileNotFoundError:
        print("Given file not found.")

