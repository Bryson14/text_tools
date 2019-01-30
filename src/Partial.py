def head(args):
    """output the first part of files"""


# a specific amount of head
    if args[0] == '-n':
        size = int(args[1])
        args = args[2:]
        for file in args:
            try:
                with open(file) as my_file:
                    data = my_file.readlines()

                # remove \n left over from .readlines()
                for i in range(len(data)):
                    data[i] = data[i][:-1]

                for i in range(size):
                    print(data[i])

            except FileNotFoundError:
                print("The file given was not located.")
            except ValueError:
                print("Argument after -n must be an integer")
            except IndexError:
                pass

# default prints 10 lines
    else:
        for file in args:
            try:
                with open(file) as my_file:
                    data = my_file.readlines()

                # remove \n left over from .readlines()
                for i in range(len(data)):
                    data[i] = data[i][:-1]

                for i in range(10):
                    print(data[i])

            except FileNotFoundError:
                print("The file given was not located.")
            except ValueError:
                print("Argument after -n must be an integer")
            except IndexError:
                pass


def tail(args):
    """output the last part of files"""

    if args[0] == '-n':
        size = int(args[1])
        args = args[2:]
        for file in args:
            try:
                with open(file) as my_file:
                    data = my_file.readlines()

                # remove \n left over from file.readlines()
                for i in range(len(data)):
                    data[i] = data[i][:-1]

                data = data[-size:]
                for i in data:
                    print(i)

            except FileNotFoundError:
                print("The file given was not located.")
            except ValueError:
                print("Argument after -n must be an integer")
            except IndexError:
                pass

    else:
        for file in args:
            try:
                with open(file) as my_file:
                    data = my_file.readlines()

                # remove \n left over from file.readlines()
                for i in range(len(data)):
                    data[i] = data[i][:-1]

                data[-10:]
                for i in data:
                    print(i)

            except FileNotFoundError:
                print("The file given was not located.")
            except ValueError:
                print("Argument after -n must be an integer")
            except IndexError:
                print("index error")

