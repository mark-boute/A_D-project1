from __future__ import print_function
import sys


def e_print(*args, **kwargs):
    """
    Prints input to sys.stderr for output in commandline
    using #! /usr/bin/python, command `./main.py`
    """
    print(*args, file=sys.stderr, **kwargs)