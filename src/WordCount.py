def wc(files: list):
    print("")
    try:
        for file in files:
            lines = words = byts = 0

            with open(file) as data:
                my_data = data.read()
            with open(file) as data:
                my_lines = data.readlines()

            # line count
            lines = len(my_lines)

            # byte count
            for c in my_data:
                byts += 1

            # word count
            # removes \n from each line because that's not useful
            for i in range(len(my_lines)):
                my_lines[i] = my_lines[i][:-1]

            word_sep = [",", ";", ":", " ", "."]

            for l in my_lines:
                words += 1
                for char in l:
                    if char in word_sep:
                        words += 1
                print(words)

            file_status(file, lines, words, byts)

    except FileNotFoundError:
        usage("\n    Given file not found.", "wc")


def file_status(file_name: str, lines: int, words: int, byts: int):
    print(lines, "   ", words, "   ", byts, "   ", file_name)
