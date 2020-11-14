"""
Algorithms and Data Structures
Practicum 1

Mark Boute      s1038503
Mark de Jong    s1034829

Subpart:
Contains functions for reading the input from the server.
"""
from common.e_print import e_print


def get_input():
    """
    Read the input and insert converted input into a dictionary.

    :return:
        python dictionary: _input
    """

    _input = dict()

    _input["nodes"] = int(input())
    _input["edges"] = int(input())
    e_print(_input["nodes"], _input["edges"])
    _input["infected"] = int(input())
    _input["infect_contact"] = float(input())

    low_up = input().split()

    _input["lower_bound"] = int(low_up[0])
    _input["upper_bound"] = int(low_up[1])

    # tests:
    assert _input["nodes"] >= 0
    assert 0 < _input["infect_contact"] < 1
    assert 0 < _input["lower_bound"] <= _input["upper_bound"]

    _input["vertices"] = get_vertices(_input["edges"])

    return _input


def get_vertices(edges: int):
    """
    get vertices from input
    :param edges: how many rows of input should be read
    :return: V, list of edge tuples.
    """
    vertices = []
    for _ in range(edges):
        vertex_input = [int(i) for i in input().split()]
        if not vertex_input[0] == vertex_input[1]:
            vertices.append(tuple(vertex_input))

    return vertices
