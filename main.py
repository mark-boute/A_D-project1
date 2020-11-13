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
from common.e_print import e_print
from common.input import get_input
from common.parser import create_adjacency_matrix
from common.girvan_newman import tests
from common.binary_search import run_bin


# for the number of inputs given by the first input
for i in range(int(input())):

    # get the remaining input for this test
    _input = get_input()

    # create an adjacency matrix from the edges given in _input
    adjacency_mat = create_adjacency_matrix(_input["edges"], _input["vertices"])

    # determine amount of clusters to be tested here, this is a placeholder for now.
    # no_of_clusters = _input["nodes"] * _input["infect_contact"] / 2

    # get a list of clusters
    # clusters = girvan_newman(adjacency_mat, no_of_clusters, _input["edges"])

    cluster = []
    for n in range(_input["nodes"]):
        cluster.append(n)

    e_print(tests(adjacency_mat, 0, _input["nodes"]))

    # evaluate no_of_clusters again because we may have received more clusters than specified
    # no_of_clusters = len(clusters)
    print("answer 0")
    failurecap = input()
    # for cluster in clusters:
    # e_print(str(i) + ":\t" + run_bin(cluster, _input["upper_bound"]) + " / " + str(_input["nodes"]))
