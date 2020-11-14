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
from common.binary_search import binary_search
from common.test import answer, test


# for the number of inputs given by the first input
for i in range(int(input())):

    # get the remaining input for this test
    _input = get_input()

    # create an adjacency matrix from the edges given in _input
    adjacency_mat = create_adjacency_matrix(_input["edges"], _input["vertices"])

    # clear some memory
    _input["vertices"] = None
    gc.collect()

    communities = None
    # get a list of unconnected graphs
    if _input["vertices"]:
        communities = get_unconnected_graphs(adjacency_mat, [n for n in range(_input["nodes"])])

    if not communities:
        communities = [n for n in range(_input["nodes"])]

    # clear some memory
    adjacency_mat = None
    gc.collect()

    if _input["infect_contact"] <= .5:

        # determine amount of clusters to be tested he
        cluster_size = 2**floor(log2(_input["nodes"]/_input["upper_bound"]-1))
        if cluster_size < 4:
            cluster_size = 4
        no_of_clusters = ceil(_input["nodes"]/cluster_size)

        clusters = []
        small_communities = []
        for community in communities:
            if isinstance(community, int):
                community = [community]
            if len(community) >= cluster_size:
                clusters.append(community)
            else:
                small_communities.append(community)

        small_clustered = []
        for small in small_communities:
            for n in small:
                small_clustered.append(n)

        while len(small_clustered) >= 2*cluster_size:
            clusters.append(small_clustered[:cluster_size])
            for _ in range(cluster_size):
                del small_clustered[0]
        clusters.append(small_clustered)

        # test
        cases = []
        for cluster in clusters:

            sub_clusters = []
            for _ in range(ceil(len(cluster)/cluster_size)):
                sub_clusters.append([])
            n = 0
            while n < len(cluster):
                sub_clusters[floor(n / cluster_size)].append(cluster[n])
                n += 1
            if len(sub_clusters[-1]) < 4:
                for n in sub_clusters[-1]:
                    sub_clusters[-2].append(n)
                    del sub_clusters[-1]

            for sub_cluster in sub_clusters:
                binary_search(sub_cluster, cases, _input["upper_bound"])
                gc.collect()

        e_print("Cluster tested: " + answer(cases))

    elif _input["infect_contact"] <= .5 and False:
        # determine amount of clusters to be tested he

        nodes = [n for n in range(_input["nodes"])]

        cluster_size = 2**floor(log2(_input["nodes"]/_input["upper_bound"]-1))
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

        cases = []
        for cluster in clusters:
            binary_search(cluster, cases, _input["upper_bound"])
            gc.collect()

        e_print("Naive Cluster tested: " + answer(cases))

    else:
        # test individually
        cases = []
        for n in range(_input["nodes"]):
            if test(n):
                cases.append(n)

        # send answer
        e_print("Individually tested: " + answer(cases))

