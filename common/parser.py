"""
Algorithms and Data Structures
Practicum 1

Mark Boute      s1038503
Mark de Jong    s1034829

Subpart:
Parse any received input and turn them into useful objects here
"""


def create_adjacency_matrix(edges: int, vertices):
    """
    Returns a numpy matrix showing connections of nodes
    :param edges: the number of edges
    :param vertices: a list of tuples containing connections of a vertex
    :return: numpy.mat
    """
    mat = []
    for _ in range(edges):
        empty_arr = []
        for _ in range(edges):
            empty_arr.append(0)
        mat.append(empty_arr)

    for vertex in vertices:
        mat[vertex[0]][vertex[1]] = 1

    return mat
