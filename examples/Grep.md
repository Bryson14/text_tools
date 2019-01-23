# Pattern search tool (`grep`)

Find all shades of Blue in our list of colors

    $ python src/tt.py grep Blue data/colors8 
    Royal Blue
    Midnight Blue
    Dodger Blue


The search pattern is case-sensitive; lowercase 'blue' is not present in our
list, hence no results are printed.

    $ python src/tt.py grep blue data/people.csv


These people like some kind of 'Blue', demonstrating that the pattern may occur
anywhere in the line.

    $ python src/tt.py grep Blue data/people.csv 
    Adrianna,22,Royal Blue,crawl
    Julian,36,Midnight Blue,traipse
    Michael,23,Dodger Blue,lurch


Find all lines containing lowercase letter 'a' across many files

    $ python src/tt.py grep a data/ages8 data/colors8 data/let3
    Favorite Color
    Royal Blue
    Light Salmon
    DarkSea Green
    Dark Goldenrod
    a


Find all lines NOT containing lowercase 'a' across many files

    $ python src/tt.py grep -v a data/ages8 data/colors8 data/let3
    Age
    22
    36
    24
    39
    26
    23
    29
    17
    Midnight Blue
    Antique White
    Dodger Blue
    Snow
    b
    c


Styles of locomotion containing the substring 'rch'

    $ python src/tt.py grep rch data/verbs8
    march
    lurch


And the rest...

    $ python src/tt.py grep -v rch data/verbs8
    Locomotion Style
    crawl
    traipse
    push
    trot
    slink
    wriggle


Words containing double 'o's; 200 lines trimmed down to 3!

    $ python src/tt.py grep oo data/words200
    clubroom
    boom
    flooding
    burglarproofed
