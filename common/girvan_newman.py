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


# Part 1: Calculate the number of edges in the graph
def __edges_in_graph(adj_mat):
    _sum = 0
    for row in adj_mat:
        _sum += sum(row)
    return _sum


# Part 2: Connected components
def __get_connected_components(adj_mat):
    pass


# Part 3: Edge betweenness
def __edge_betweenness(adj_mat):
    # for v in V:
    for row in range(adj_mat.size[0]):
        for col in range(adj_mat.size[0]):
            if adj_mat[row][col] == 1:
                # do
                pass

    S = ["to", "be", "determined"]
    # while S not empty do:
    while S:
        # pop w <- S

        pass
        # for v in Pred[w] do:


# Part 4: Girvan-Newman
def girvan_newman(adj_mat, clusters: int, edges=None):
    """
    Splits graph into $clusters$ or more relatively dense components

    :param adj_mat: adjacency matrix representing graph
    :param clusters: number of desired clusters
    :param OPTIONAL edges: number of edges in the graph
    :return: clusters of nodes as a list of tuples,
            the amount of clusters may be higher that originally specified.
    """
    # if no edges, then return. * No clusters *
    if adj_mat.max() == 0:
        return

    # protect graph data by making a copy.
    graph = adj_mat.copy()

    # 1. while number of connected sub-graphs < specified number of clusters
    #    and the number of edges in graph > 0:
    connected_sub_graphs = 0
    while connected_sub_graphs < clusters and graph.max() > 0:
        # 2. calculate edge betweenness for every edge in the graph
        edge_betweenness(graph)

        # 3. remove edge(s) with highest betweenness

        # 4. recalculate connected components


def edge_betweenness(graph):
    pass
