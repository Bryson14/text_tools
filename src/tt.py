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


    if len(sys.argv) < 2:
        print("Usage: src/tt.py FUNCTION [FILE/S] \nEnter the function name to get a list of commands "
              "\n==========\n FUNCTIONS\n==========\n"
              "cat - concatenates two or more files together separated my new lines\n"
              "tac - the same as CAT but in reverse order\n"
              "cut - cuts a column/s from a csv format\n"
              "paste - combines two or more files into csv format\n"
              "grep - finds a specified string across one or many files, and returns the line they are found on\n"
              "head - returns the first n lines of a file\n"
              "tail - returns the last n lines of a file\n"
              "sort - sorts a file alphabetically\n"
              "uniq - returns the lines that are unique in a file\n"
              "wc - returns the number of lines, words, and characters in a file/s\n"
              "usage")
        sys.exit(1)
    elif str(sys.argv[2]).lower() in functions:
        pass
    else:
        print("Function does not exist")



