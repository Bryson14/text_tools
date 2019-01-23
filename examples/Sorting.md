# Sorting files and detecting duplicates (`sort` and `uniq`)

`sort` prints its output files sorted in alphabetical order

    $ python src/tt.py sort data/colors8
    Antique White
    Dark Goldenrod
    DarkSea Green
    Dodger Blue
    Favorite Color
    Light Salmon
    Midnight Blue
    Royal Blue
    Snow


The results are surprising when one forgets that `sort` performs alphabetic
sorting:

    $ python src/tt.py sort data/random20
    1
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    2
    20
    3
    4
    5
    6
    7
    8
    9


Reverse sorted data can be obtained by first sorting in order with the `sort`
tool, then reversing the result with `tac`:

    $ python src/tt.py sort data/colors8 > sortedColors8

    $ python src/tt.py tac sortedColors8
    Snow
    Royal Blue
    Midnight Blue
    Light Salmon
    Favorite Color
    Dodger Blue
    DarkSea Green
    Dark Goldenrod
    Antique White


The `uniq` tool detects duplicated lines in its input.  It expects its input to
be already sorted, meaning it can only detect duplicates that are adjacent in
the file.

By default it removes duplicates from its input

    $ python src/tt.py uniq data/dup5
    1
    2
    3
    4
    5


Given the `-c` flag `uniq` will count the number of occurrences of each line
encountered:

    $ python src/tt.py uniq -c data/dup5
          2 1
          2 2
          1 3
          2 4
          1 5


When given the `-D` flag it prints only the duplicated lines
    $ python src/tt.py uniq -D data/dup5
    1
    1
    2
    2
    4
    4


When given the `-u` flag it only prints unique lines
    $ python src/tt.py uniq -u data/dup5
    3
    5


Use `uniq` in conjunction with the `sort` tool to identify redundant data:
    $ python src/tt.py sort data/words200 > sortedWords


    $ python src/tt.py uniq -D sortedWords
    finders
    finders
    keepers
    keepers
    losers
    losers
    weepers
    weepers
