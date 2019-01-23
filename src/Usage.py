# Usage instructions and descriptions for each tool

CAT = """tt.py cat|tac FILENAME...
        Concatenate and print files in order or in reverse"""


CUT = """tt.py cut [-f LIST] FILENAME...
        Remove comma-separated sections from each line of files
        -f  List of comma-separated integers indicating fields to output"""


PASTE = """ttt.py paste FILENAME...
        Merge lines of files into one comma-separated text"""
            

GREP = """tt.py grep [-v] PATTERN FILENAME...
        Print lines of files matching PATTERN
        -v  Invert matching; print lines which DO NOT match PATTERN"""


HEAD = """tt.py head|tail [-n N] FILENAME...
        Output the first or last part of files
        -n  Number of lines to print (default is 10)"""


SORT = """tt.py sort FILENAME...
        Output lines of text file in sorted order"""


UNIQ = """tt.py uniq [-c|-D|-u] FILENAME...
        Report or omit repeated lines in files
        -c  Count number of consecutive occurances
        -D  Print only duplicated lines; omit unique lines
        -u  Print only unique lines; omit duplicated lines"""


WC = """tt.py wc FILENAME...
        Print newline, word, and byte counts for each file"""


# Store messages in a dictionary for easy look-up
messages = {
        'cat': CAT,
        'tac': CAT,

        'cut': CUT,
        'paste': PASTE,

        'grep': GREP,

        'head': HEAD,
        'tail': HEAD,

        'sort': SORT,
        'uniq': UNIQ,

        'wc': WC,
        }



def usage(error=None, tool=None):
    """Provied a unified error reporting interface"""
    # Print a specific error message, if provided
    if error is not None:
        print(f"Error: {error}\n")
    
    # Print a tool-specific message where possible; otherwise, display
    # instructions for all tools
    if tool is None or tool not in messages:
        print("Python Text Tools Usage:")
        for msg in [CAT, CUT, PASTE, GREP, HEAD, SORT, UNIQ, WC]:
            print(f"    {msg}\n")
    else:
        print(messages[tool])
