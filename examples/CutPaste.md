# Cut and Paste tools (`cut` and `paste`)

Paste joins two or more files together, inserting a comma in between

    $ python src/tt.py paste data/let3 data/num2 
    a,1
    b,2
    c,


The output is as long as the longest file; missing fields are simply left out

    $ python src/tt.py paste data/num2 data/let3 
    1,a
    2,b
    ,c


    $ python src/tt.py paste data/num2 data/let3 data/words5 
    1,a,babbles
    2,b,sneakiness
    ,c,trimly
    ,,agree
    ,,frankly


    $ python src/tt.py paste data/num2 data/words5 data/let3
    1,babbles,a
    2,sneakiness,b
    ,trimly,c
    ,agree,
    ,frankly,


When only one file is given `paste` behaves like `cat`

    $ python src/tt.py paste data/num10
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10


If any of the input files does not exist, the entire operation fails

    $ python src/tt.py paste data/num2 data/DOES_NOT_EXIST data/let3 
    Traceback (most recent call last):
      File "src/tt.py", line 69, in <module>
        ops[sys.argv[1]](sys.argv[2:])
      File "/home/fadein/school/Sp19/cs1440/Assn/2/src/CutPaste.py", line 40, in paste
        f = open(fil)
    FileNotFoundError: [Errno 2] No such file or directory: 'data/DOES_NOT_EXIST'


`paste` is used to create Comma Separated Values (CSV) files

    $ python src/tt.py paste data/num10  data/names10 data/words5
    1,Jerry,babbles
    2,Bailey,sneakiness
    3,Frank,trimly
    4,Kai,agree
    5,Angela,frankly
    6,Mikayla,
    7,Hazel,
    8,Karen,
    9,Alexa,
    10,Isabel,


The resulting data can be redirected to a new file with the shell's redirection
operator >.  The output then goes into the file instead of the screen.

    $ python src/tt.py paste data/num10  data/names10 data/words5 > data/kids.csv


This is how I created the file `data/people.csv`

    $ python src/tt.py paste data/names8 data/ages8 data/colors8 data/verbs8 > data/people.csv


`cut`, in contrast to `paste`, extracts fields (or columns) of data from a CSV
file.  By default the 1st column is extracted

    $ python src/tt.py cut data/people.csv
    Name 
    Adrianna 
    Julian 
    Tiffany 
    Savannah 
    Abraham 
    Michael 
    Marcus 
    Julianna 


Use the `-f` flag to specify which field to extract

    $ python src/tt.py cut -f 2 data/people.csv
    Age 
    22 
    36 
    24 
    39 
    26 
    23 
    29 
    17 


A list of fields (possibily non-consecutive) may be specified.  Separate each
field in the list with commas.

    $ python src/tt.py cut -f 2,4 data/people.csv
    Age,Locomotion Style 
    22,crawl 
    36,traipse 
    24,push 
    39,march 
    26,trot 
    23,lurch 
    29,slink 
    17,wriggle 


Although the user specified an out-of-order list, `cut` will print the fields
in the ascending order, as though the field specification is sorted within the
program.

    $ python src/tt.py cut -f 4,2 data/people.csv
    Age,Locomotion Style 
    22,crawl 
    36,traipse 
    24,push 
    39,march 
    26,trot 
    23,lurch 
    29,slink 
    17,wriggle 


Notice the excess of blank lines produced from this file; half of the lines in
`data/kids.csv` have a blank 3rd field.

    $ python src/tt.py cut -f 3 data/kids.csv
    babbles 
    sneakiness 
    trimly 
    agree 
    frankly 
     
     
     
     
     
