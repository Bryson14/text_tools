from Usage import usage


def cut(args):
    """remove sections from each line of files"""

    if args[0] == "-f":

        # takes in one or multiple column args.
        iden = str(args[1])

        iden = iden.split(",")
        try:
            for i in range(len(iden)):
                iden[i] = int(iden[i])
        except ValueError:
            usage("Indexes must be positive integers.", "cut")

        # print multiple specific columns
        if len(iden) > 1:
            print_cut(args[2], iden)

        # print one specific column
        else:
            print_cut(args[2], iden[0])

    else:
        print_cut(args[0], 0)


def print_cut(file, column):
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
            try:
                for line in lines:
                    print(line[column])
            except IndexError:
                usage("The index you attempted doesn't exist in this file.", "cut")

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

    data = []
    for file in args:
        try:
            with open(file) as stuff:
                lines = stuff.readlines()

            # remove \n left over from .readlines()
            for i in range(len(lines)):
                lines[i] = lines[i][:-1]

            data.append(lines)

        except FileNotFoundError:
            usage("File not found.", "paste")

    # find the longest file
    max = 0
    for cell in data:
        if len(cell) > max:
            max = len(cell)

    # prints the file in the correct csv format
    for i in range(max):
        for j in range(len(data)):
            if i < len(data[j]):
                print(data[j][i], end="")
            if j < len(data) - 1:
                print(",", end="")
        print("")
