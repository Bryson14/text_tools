# Printing portions of a file (`head` and `tail`)

`head` prints the first 10 lines of a file.  If the file is less than or equal
to 10 lines long, `head` operates the same as `cat`

    $ python src/tt.py head data/let3
    a
    b
    c


    $ python src/tt.py head data/names10
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


    $ python src/tt.py head data/words200 
    social
    insomniac
    implicitly
    cranky
    opponents
    clubroom
    uttering
    roughen
    easter
    dad



A different limit than 10 may be provided with the `-n` argument

    $ python src/tt.py head -n 13 data/words200
    social
    insomniac
    implicitly
    cranky
    opponents
    clubroom
    uttering
    roughen
    easter
    dad
    sleighs
    honoraries
    smelt


    $ python src/tt.py head -n 1 data/words200
    social


`tail`, by contrast, prints the final 10 (or N) lines of a file:

    $ python src/tt.py tail data/let3
    a
    b
    c


    $ python src/tt.py tail data/words200
    convicting
    exacerbating
    indictment
    very
    impersonated
    latching
    reconfigurations
    activates
    autobiographies
    adverbs


    $ python src/tt.py tail -n 4 data/words200
    reconfigurations
    activates
    autobiographies
    adverbs


    $ python src/tt.py tail -n 1 data/words200
    adverbs


Combining these tools enables one to extract a portion from the middle of a
large file.  Here we extract words 80 - 97 from a list of 200 words:

    $ python src/tt.py head -n 97 data/words200 > first97
    $ python src/tt.py tail -n 17 first97
    chrysanthemum
    malts
    draughts
    sterilizes
    hydrogen
    even
    pulsate
    upland
    outperforms
    subprogram
    lustiness
    handicap
    boom
    inhabiting
    improviser
    musicals
    the
