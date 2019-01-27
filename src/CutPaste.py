from Usage import usage


def cut(args):
    """remove sections from each line of files"""

    if args[0] == "-f":

        # takes in one or multiple column args.
        iden = str(args[1])

        iden = iden.split(",")
        for i in range(len(iden)):
            iden[i] = int(iden[i])
        print(iden)

        # print multiple specific columns
        if len(iden) > 1:
            print_cut(args[2], iden)


        # print one specific column
        else:
            print("only one column")
            print_cut(args[2], iden[0])


    else:
        print_cut(args[0], 0)


def print_cut(file, column: list):
    try:
        with open(file) as data:
            lines = data.readlines()

        # remove \n left over from .readlines()
        for i in range(len(lines)):
            lines[i] = lines[i][:-1]

        # splits lines by commas into lists
        for i in range(len(lines)):
            lines[i] = lines[i].split(",")

        # prints one column
        if not isinstance(column, list):
            for line in lines:
                print(line[column])

        # prints multiple columns
        else:
            for line in lines:
                for i in range(len(column)):
                    print(line[column[i]], end="")
                    if i < len(column) - 1:
                        print(", ", end="")
                print("")


    except FileNotFoundError:
        usage("File not found", "cut")


def paste(args):
    """merge lines of files"""



