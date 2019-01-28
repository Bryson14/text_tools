from Usage import usage


def sort(args):
    """sort lines of text files"""
    for file in args:
        try:
            with open(file) as data:
                lines = data.readlines()

            # remove \n left over from .readlines()
            for i in range(len(lines)):
                lines[i] = lines[i][:-1]

            for i in sorted(lines):
                print(i)

        except FileNotFoundError:
            usage("File not found", "sort")



def uniq(args):
    """report or omit repeated lines"""

# prints only the unique lines
    if args[0] == "-u":
        files = args[1:]
        for file in files:
            omit_copies(file)

# prints only the duplicates lines
    elif args[0] == "-D":
        files = args[1:]
        for file in files:
            omit_uniq(file)

# returns the # of occurrences of each line
    elif args[0] == "-c":
        files = args[1:]
        for file in files:
            count(file)

# prints every line only once despite duplicates
    else:
        for file in args:
            once = only_once(file)
            for word in once:
                print(word)


def omit_copies(file):
    lst = word_list(file)
    for i in range(len(lst)):
        j = i + 1

        # end of list
        if j > len(lst):
            if lst[i] != list[j -2]:
                print(lst[i])

        # does not print line i
        elif lst[i] == lst[j]:
            pass

        else:
            print(lst[i])


def omit_uniq(file):
    lst = word_list(file)
    for i in range(len(lst)):
        j = i + 1

        # end of list
        if j >= len(lst):
            if lst[i] != lst[j - 2]:
                print(lst[i])

        # print line i with dup
        elif lst[i] == lst[j]:
            print(lst[i])

        # backwards check
        elif i > 0:
            if lst[i] == lst[j -2]:
                print(lst[i])
        else:
            pass


def count(file):
    word_lst = word_list(file)
    uniqs = only_once(file)
    occur = []

    # makes a separate list with the number of occurrences
    for unq in uniqs:
        occur.append(word_lst.count(unq))

    for i in range(len(occur)):
        print(occur[i], " : ", word_lst[i])


def only_once(file) -> list:
    lst = word_list(file)
    once_lst = []
    for i in range(len(lst)):
        j = i - 1

        # beginning of list
        if j < 0:
            once_lst.append(lst[i])

        # backwards check
        elif i > 0:
            if lst[i] != lst[j]:
                once_lst.append(lst[i])
        else:
            pass

    return once_lst


def word_list(file) -> list:
    try:
        with open(file) as data:
            data = data.read()

        data = data.split("\n")
        word_sep = [",", ";", ":", " ", "."]

        wordlist = []
        i = 0
        for line in data:
            wordlist.append("")
            for char in line:
                if char not in word_sep:
                    wordlist[i] = wordlist[i] + char
                else:
                    i += 1
                    wordlist.append("")
            i += 1

        # removes that "" that are left over. Its easier to do this than something else haha
        while "" in wordlist:
            wordlist.remove("")

        return wordlist

    except FileNotFoundError:
        usage("File not found", "sort")
