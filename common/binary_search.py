"""
Algorithms and Data Structures
Practicum 1

Mark Boute      s1038503
Mark de Jong    s1034829

Subpart: Binary Search

"""
from common.e_print import e_print


def test(nodes):
    output = "test"
    for n in nodes:
        output = output + " " + str(n)
    e_print(output)
    return bool(input())


def binary_search(nodes, positive_cases):
    if len(nodes) == 1:
        # positive case
        positive_cases.append(nodes[0])
    else:
        middle_index = len(nodes)//2

        first_half = nodes[:middle_index]
        second_half = nodes[middle_index:]
        if test(first_half):
            binary_search(first_half)
        if test(second_half):
            binary_search(second_half)


def run_bin(nodes):
    positive_cases = []
    binary_search(nodes, positive_cases)
    output = "answer"
    for c in positive_cases:
        output = output + " " + str(c)
    e_print(output)
    return input()
