"""
Algorithms and Data Structures
Practicum 1

Mark Boute      s1038503
Mark de Jong    s1034829

Subpart: Binary Search

"""
from common.test import test


def binary_search(cluster, to_be_examined, cases):
    # return list of cases

    # base_case
    if len(cluster) == 1:
        del to_be_examined[0]
        cases.append(cluster[0])
        if len(to_be_examined) > 0:
            if test(to_be_examined):
                binary_search(cluster, to_be_examined, cases)

    # recursive case
    else:
        middle_index = len(cluster) // 2
        first_half = cluster[:middle_index]
        second_half = cluster[middle_index:]
        if test(first_half):
            binary_search(first_half, to_be_examined, cases)
        else:
            if test(second_half):
                binary_search(second_half, to_be_examined, cases)


def old_binary_search(nodes, positive_cases, infected):
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
            old_binary_search(first_half, positive_cases, infected)
        if test(second_half):
            old_binary_search(second_half, positive_cases, infected)
