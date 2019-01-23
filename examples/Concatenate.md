# Forward and reverse concatenation tools (`cat` and `tac`)

Concatenate two files into one output

    $ python src/tt.py cat data/let3 data/num2 
    a
    b
    c
    1
    2


Ordinarily, `cat` is used by Unix hackers to print a file to the screen

    $ python src/tt.py cat data/names10 
    Jerry
    Bailey
    Frank
    Kai
    Angela
    Mikayla
    Hazel
    Karen
    Alexa
    Isabel


An error is signaled when a non-existent file is named

    $ python src/tt.py cat data/DOES_NOT_EXIST
    Traceback (most recent call last):
      File "src/tt.py", line 69, in <module>
        ops[sys.argv[1]](sys.argv[2:])
      File "/home/fadein/school/Sp19/cs1440/Assn/2/src/Concatenate.py", line 4, in cat
        f = open(fl, 'r');
    FileNotFoundError: [Errno 2] No such file or directory: 'data/DOES_NOT_EXIST'


Your program must detect and report the case where too few arguments are given;
at a minimum the name of an input file is required:

    $ python src/tt.py cat
    Error: Too few arguments

    tt.py cat|tac FILENAME...
            Concatenate and print files in order or in reverse


`tac` works just like `cat`, only backwards

    $ python src/tt.py tac data/let3 data/num2 
    c
    b
    a
    2
    1



    $ python src/tt.py tac data/names10 
    Isabel
    Alexa
    Karen
    Hazel
    Mikayla
    Angela
    Kai
    Frank
    Bailey
    Jerry


Just like `cat`, `tac` (and indeed, all utilities) let Python raise an error
when a non-existent file is named on the command line as well as when too few
arguments are provided:

    $ python src/tt.py tac data/DOES_NOT_EXIST
    Traceback (most recent call last):
      File "src/tt.py", line 69, in <module>
        ops[sys.argv[1]](sys.argv[2:])
      File "/home/fadein/school/Sp19/cs1440/Assn/2/src/Concatenate.py", line 13, in tac
        f = open(fl)
    FileNotFoundError: [Errno 2] No such file or directory: 'data/DOES_NOT_EXIST'


    $ python src/tt.py tac
    Error: Too few arguments

    tt.py cat|tac FILENAME...
            Concatenate and print files in order or in reverse
