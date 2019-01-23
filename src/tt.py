#!/usr/bin/env python

from Concatenate import cat, tac
from CutPaste import cut, paste
from Grep import grep
from Partial import head, tail
from Sorting import sort, uniq
from WordCount import wc
from Usage import usage

import sys



if len(sys.argv) < 2:
    usage()
    sys.exit(1)
