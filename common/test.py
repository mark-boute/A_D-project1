"""
Algorithms and Data Structures
Practicum 1

Mark Boute      s1038503
Mark de Jong    s1034829

Subpart: requesting tests and answering cases
"""


def test(nodes):
    if isinstance(nodes, int):
        print("test " + str(nodes))
    else:
        output = "test"
        for n in nodes:
            output = output + " " + str(n)
        print(output)

    return input() == "true"


def answer(nodes):
    if isinstance(nodes, int):
        print("answer " + str(nodes))
    else:
        output = "answer"
        for n in nodes:
            output = output + " " + str(n)
        print(output)
    return input()
