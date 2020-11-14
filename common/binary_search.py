"""
Algorithms and Data Structures
Practicum 1

Mark Boute      s1038503
Mark de Jong    s1034829

Subpart: Binary Search

"""
from common.test import test


def binary_search(nodes, unconfirmed_cases, cases):

    if len(nodes) == 1 and not len(unconfirmed_cases) > 1:
        cases.append(nodes[0])
        if nodes[0] in unconfirmed_cases:
            unconfirmed_cases.remove(nodes[0])

    elif len(nodes) == 1 and len(unconfirmed_cases) > 1:
        cases.append(nodes[0])
        if nodes[0] in unconfirmed_cases:
            unconfirmed_cases.remove(nodes[0])
        if test(unconfirmed_cases):
            binary_search(nodes, unconfirmed_cases, cases)

    else:
        middle_index = len(nodes) // 2
        first_half = nodes[:middle_index]
        second_half = nodes[middle_index:]
        if test(first_half):
            binary_search(first_half, unconfirmed_cases, cases)
        else:
            if test(second_half):
                binary_search(second_half, unconfirmed_cases, cases)


def old_binary_search(nodes, positive_cases, infected):
    if len(positive_cases) >= infected:
        return

    if len(nodes) == 1:
        # positive case
        positive_cases.append(nodes[0])
    elif len(nodes) == 2:
        print("test " + str(nodes[0]))
        if not input() == "true":
            positive_cases.append(nodes[1])
        else:
            positive_cases.append(nodes[0])
            print("test " + str(nodes[1]))
            if input() == "true":
                positive_cases.append(nodes[1])
    else:
        middle_index = len(nodes)//2

        first_half = nodes[:middle_index]
        second_half = nodes[middle_index:]
        if test(first_half):
            old_binary_search(first_half, positive_cases, infected)
        if test(second_half):
            old_binary_search(second_half, positive_cases, infected)
