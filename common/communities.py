"""
Algorithms and Data Structures
Practicum 1

Mark Boute      s1038503
Mark de Jong    s1034829

Subpart:
This part contains the implementation of the Girvan-Newman algorithm
( https://en.wikipedia.org/wiki/Girvan%E2%80%93Newman_algorithm )

Pseudocode is a subset from ( https://www.cl.cam.ac.uk/teaching/1718/MLRD/tasks/task12.html ):

Part 1: Calculate the number of edges in the graph
    Determine the number of edges in the graph.

Part 2: Connected components
    Implement a depth-first search algorithm to check for connectivity
    and then use it to find all connected components in the graph.
    (Two nodes are in the same connected component iff there is a path between them.)

Part 3: Edge betweenness
    Implement edge betweenness.
    ( As by pseudocode givin in section 3.5 from
        http://www.sciencedirect.com/science/article/pii/S0378873307000731 )

Part 4: Girvan-Newman
    1. while number of connected sub-graphs < specified number of clusters
       and the number of edges in graph > 0:
    2. calculate edge betweenness for every edge in the graph
    3. remove edge(s) with highest betweenness
    4. recalculate connected components
"""
from common.e_print import e_print


def get_shortest_paths(adj_mat, node, nodes):
    nodes_to_evaluate = nodes.copy()
    nodes_to_evaluate.remove(node)
    level_nodes = [node]

    shortest_paths = [0 for _ in range(len(nodes))]

    found_new_nodes = True

    while nodes_to_evaluate and found_new_nodes:
        found_new_nodes = False
        evaluated = []
        for level_node in level_nodes:
            for adj_mat_node in nodes_to_evaluate:
                if adj_mat[level_node][adj_mat_node] == 1:
                    shortest_paths[nodes_to_evaluate.index(adj_mat_node)] += 1
                    if adj_mat_node not in evaluated:
                        evaluated.append(adj_mat_node)
        for e in evaluated:
            if e in nodes_to_evaluate:
                nodes_to_evaluate.remove(e)
                found_new_nodes = True
        level_nodes = evaluated

    for not_connected in nodes_to_evaluate:
        shortest_paths[nodes_to_evaluate.index(not_connected)] = -1

    return shortest_paths


def get_unconnected_graphs(adj_mat, nodes_in):
    communities = []
    nodes = nodes_in.copy()

    while nodes:
        community = []
        unconnected = []

        shortest_paths = get_shortest_paths(adj_mat, nodes[0], nodes)

        for n in range(len(nodes)):
            if shortest_paths[n] >= 0:
                community.append(nodes[n])
            else:
                unconnected.append(nodes[n])

        communities.append(community)
        nodes = unconnected

    # e_print("Communities:")
    # e_print(communities)
    return communities


def tests(adj_mat, node, no_of_nodes):
    current_max = 0
    for row in adj_mat:
        if max(row) == 1:
            current_max = 1
            break
    return get_shortest_paths(adj_mat, node, no_of_nodes)
