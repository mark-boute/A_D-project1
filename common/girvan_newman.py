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


def __shortest_paths(adj_mat, node, no_of_nodes):
    nodes_to_evaluate = []
    shortest_paths = []
    for n in range(no_of_nodes):
        nodes_to_evaluate.append(n)
        shortest_paths.append(0)

    nodes_to_evaluate.remove(node)
    shortest_paths[node] = 0

    found_new_nodes = True
    level_nodes = [node]
    while nodes_to_evaluate and found_new_nodes:
        found_new_nodes = False
        evaluated = []
        for level_node in level_nodes:
            for adj_mat_node in nodes_to_evaluate:
                if len(adj_mat) <= level_node:
                    e_print("row", len(adj_mat), level_node)
                if len(adj_mat[level_node]) <= adj_mat_node:
                    e_print("col", len(adj_mat[level_node]), adj_mat_node)

                if adj_mat[level_node][adj_mat_node] == 1:
                    shortest_paths[adj_mat_node] += 1
                    if adj_mat_node not in evaluated:
                        evaluated.append(adj_mat_node)
        for e in evaluated:
            if e in nodes_to_evaluate:
                nodes_to_evaluate.remove(e)
                found_new_nodes = True
        level_nodes = evaluated
        e_print("Nodes to eval = " + str(len(nodes_to_evaluate)))

    for not_connected in nodes_to_evaluate:
        shortest_paths[not_connected] = -1

    levellist = []
    for _ in range(max(shortest_paths)+1):
        levellist.append([])

    for i in range(len(shortest_paths)):
        if shortest_paths[i] >= 0:
            levellist[shortest_paths[i]].append(i)

    for level in levellist:
        e_print(level)

    return shortest_paths


def tests(adj_mat, node, no_of_nodes):
    current_max = 0
    for row in adj_mat:
        if max(row) == 1:
            current_max = 1
            break
    if current_max == 0 or no_of_nodes > 100:
        return "No connections or too large"
    return __shortest_paths(adj_mat, node, no_of_nodes)
