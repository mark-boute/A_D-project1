#! /usr/bin/python

"""
Algorithms and Data Structures
Practicum 1

Mark Boute      s1038503
Mark de Jong    s1034829

Main:
Ties everything together for execution on the test server

To test on server:
    `ncat -c "echo $USERNAME && echo $PASSWORD && ./main.py" group-testing.maarse.xyz 6525 -o o.txt`
"""
from __future__ import print_function
import sys

from common.input import get_input
from common.parser import create_adjacency_matrix


def e_print(*args, **kwargs):
    """
    Prints input to sys.stderr for output in commandline
    using #! /usr/bin/python, command `./main.py`
    """
    print(*args, file=sys.stderr, **kwargs)


for _ in range(int(input())):
    _input = get_input()
    adjacency_mat = create_adjacency_matrix(_input["edges"], _input["vertices"])
