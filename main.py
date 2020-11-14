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
import gc

from math import floor, ceil, log2

from common.e_print import e_print
from common.input import get_input
from common.parser import create_adjacency_matrix
from common.communities import get_unconnected_graphs
from common.binary_search import old_binary_search
from common.test import answer


# for the number of inputs given by the first input
for i in range(int(input())):

    # get the remaining input for this test
    _input = get_input()

    # create an adjacency matrix from the edges given in _input
    adjacency_mat = create_adjacency_matrix(_input["edges"], _input["vertices"])

    # clear some memory
    _input["vertices"] = len(_input["vertices"])
    e_print(_input["vertices"])
    gc.collect()

    communities = None
    # get a list of unconnected graphs
    if not _input["vertices"] == 0:
        communities = get_unconnected_graphs(adjacency_mat, [n for n in range(_input["nodes"])])

    # clear some memory
    adjacency_mat = None
    gc.collect()

    if _input["infect_contact"] <= 0.5:

        # determine amount of clusters to be tested he
        cluster_size = 2**floor(log2(1/_input["infect_contact"]-1))
        if cluster_size < 4:
            cluster_size = 4
        no_of_clusters = ceil(_input["nodes"]/cluster_size)

        clusters = []
        for _ in range(no_of_clusters):
            clusters.append([])

        n = 0
        while n < _input["nodes"]:
            clusters[floor(n/cluster_size)].append(n)
            n += 1

        # test clusters
        cases = []
        for cluster in clusters:
            old_binary_search(cluster, cases, _input["upper_bound"])
            gc.collect()

        e_print(answer(cases))

        # e_print(tests(adjacency_mat, 0, _input["nodes"]))

        # evaluate no_of_clusters again because we may have received more clusters than specified
        # no_of_clusters = len(clusters)

        #for cluster in clusters:
        #   e_print(str(i) + ":\t" + run_bin(cluster, _input["upper_bound"]) + " / " + str(_input["nodes"]))

    else:
        # test individually
        cases = []
        for n in range(_input["nodes"]):
            print("test " + str(n))
            if input() == "true":
                cases.append(n)

        # send answer
        e_print(answer(cases))
