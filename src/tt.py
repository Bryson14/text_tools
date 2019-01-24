#!/usr/bin/env python

from Concatenate import cat, tac
from CutPaste import cut, paste
from Grep import grep
from Partial import head, tail
from Sorting import sort, uniq
from WordCount import wc
from Usage import usage

import sys
import os.path as path

functions = ["cat", "tac", "cut", "paste", "grep", "head", "tail", "sort", "uniq", "wc", "usage"]

if __name__ == "__main__":

    # too little arguments
    if len(sys.argv) < 2:
        usage("Not enough arguments given")
        sys.exit(1)

    # no files were given to an attempted function
    elif len(sys.argv) == 2:
        usage(None, str(sys.argv[1]).lower())
        sys.exit(1)

    # initializes the correct function
    elif str(sys.argv[1]).lower() in functions:
        args = []
        for arg in sys.argv:
            args.append(arg)
        args = args[2:]

        func = str(sys.argv[1]).lower()

        # calls the correct function
        if func == "cat":
            cat(args)
        elif func == "tac":
            tac(args)
        elif func == "cut":
            cut(args)
        elif func == "paste":
            paste(args)
        elif func == "grep":
            grep(args)
        elif func == "head":
            head(args)
        elif func == "tail":
            tail(args)
        elif func == "sort":
            sort(args)
        elif func == "uniq":
            uniq(args)
        else:
            wc(args)

    # unidentified function call
    else:
        usage("Function is not an identified call")
        sys.exit(1)



