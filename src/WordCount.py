def wc(files: list):
    print("")
    try:
        for file in files:
            lines = words = byts = 0

            with open(file) as data:
                my_data = data.read()
            with open(file) as data:
                my_lines = data.readlines()

            lines = len(my_lines)

            for c in my_data:
                byts += 1

            my_data.replace(",", "\n")
            my_data.replace(" ", "\n")
            for thing in my_data.split("\n"):
                print("i:", thing)
            words = len(my_data.split("\n"))

            file_status(file, lines, words, byts)

    except FileNotFoundError:
        usage("\n    Given file not found.", "wc")


def file_status(file_name: str, lines: int, words: int, byts: int):
    print(lines, "   ", words, "   ", byts, "   ", file_name)
