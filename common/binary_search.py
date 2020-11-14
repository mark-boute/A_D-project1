"""
Algorithms and Data Structures
Practicum 1

Mark Boute      s1038503
Mark de Jong    s1034829

Subpart: Binary Search

"""
from common.test import test


def b_binary_search(nodes):
    if len(nodes) == 1:
        return nodes[0]

    middle_index = len(nodes) // 2
    a = nodes[:middle_index]
    b = nodes[middle_index:]
    if test(a):
        return b_binary_search(a)
    else:
        for n in a:
            nodes.remove(n)
        return b_binary_search(b)


def binary_search(nodes, positive_cases, infected):
    if len(positive_cases) >= infected:
        return

    if len(nodes) == 1:
        positive_cases.append(nodes[0])
    elif len(nodes) == 2:
        if not test(nodes[0]):
            positive_cases.append(nodes[1])
        else:
            positive_cases.append(nodes[0])
            if test(nodes[1]):
                positive_cases.append(nodes[1])
    else:
        middle_index = len(nodes)//2

        first_half = nodes[:middle_index]
        second_half = nodes[middle_index:]
        if test(first_half):
            binary_search(first_half, positive_cases, infected)
        if test(second_half):
            binary_search(second_half, positive_cases, infected)
