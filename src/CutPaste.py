from Usage import usage


def cut(args):
    """remove sections from each line of files"""

    if args[0] == "-f":

        # takes in one or multiple column args
        iden = str(args[1])
        if "," in iden:
            iden.split(",")
        else:
            iden = int(iden)

    else:
        print_cut(args[0])

def print_cut(file):
    try:
        with open(file) as data:
            lines = data.readlines()

        # remove \n left over from .readlines()
        for i in range(len(lines)):
            lines[i] = lines[i][:-1]

        # splits lines by commas into lists
        for i in range(len(lines)):
            lines[i] = lines[i].split(",")

        for line in lines:
            print(line[0])

    except FileNotFoundError:
        usage("File not found", "cut")


def paste(args):
    """merge lines of files"""



