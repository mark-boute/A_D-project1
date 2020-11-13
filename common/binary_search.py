"""
Algorithms and Data Structures
Practicum 1

Mark Boute      s1038503
Mark de Jong    s1034829

Subpart: Binary Search

"""
tested = 0


def test(nodes):
    global tested
    tested += 1
    output = "test"
    for n in nodes:
        output = output + " " + str(n)
    print(output)
    return input() == "true"


def binary_search(nodes, positive_cases, infected):
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
            binary_search(first_half, positive_cases, infected)
        if test(second_half):
            binary_search(second_half, positive_cases, infected)


def run_bin(nodes, infected):
    global tested
    tested = 0
    positive_cases = []
    binary_search(nodes, positive_cases, infected)

    output = "answer"
    for c in positive_cases:
        output = output + " " + str(c)
    print(output)
    return str(len(positive_cases)) + "\t" + input() + "\t" + str(tested)
