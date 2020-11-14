"""
Algorithms and Data Structures
Practicum 1

Mark Boute      s1038503
Mark de Jong    s1034829

Subpart: Find unconnected communities in graphs
"""


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

    return communities
