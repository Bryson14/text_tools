from Usage import usage


def wc(files: list):
    print("")
    file_status("file name", "lines", "words", "bytes")
    try:
        for file in files:
            lines = words_real = byts = words_linux = 0

            with open(file) as data:
                my_data = data.read()
            with open(file) as data:
                my_lines = data.readlines()

            # line count
            lines = len(my_lines)

            # byte count
            for c in my_data:
                byts += 1

            # word count by linux conventions for assn 2
            for line in my_lines:
                words_linux += len(line.split(" "))

            # word count real not dumb linux conventions.
            # removes \n from each line because that's not useful
            data = my_data.split("\n")
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

            # removes that "" that are left over. Its easier to do this
            while "" in wordlist:
                wordlist.remove("")

            words_real = len(wordlist)

            file_status(file, lines, words_linux, byts)

    except FileNotFoundError:
        usage("\n    Given file not found.", "wc")


def file_status(file_name: str, lines: int, words: int, byts: int):
    print('{:6}'.format(lines), '{:6}'.format(words), '{:6}'.format(byts), '{:>20}'.format(file_name))

