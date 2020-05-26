import networkx as nx
import numpy as np
import matplotlib
import random


def bk(graph, P, R=set(), X=set()):
    bk.count += 1
    if not any((P, X)):
        yield R
    for node in P.copy():
        for r in bk(graph, P.intersection(graph.neighbors(node)),
                    R=R.union(set([node])), X=X.intersection(graph.neighbors(node))):
            yield r
        P.remove(node)
        X.add(node)


def bk_pivot(graph, P, R=set(), X=set()):
    bk_pivot.count += 1
    if not any((P, X)):
        yield R
    P_copy = P.copy()
    pivot = random.choice(list(graph))
    #pivot = int(str(random.sample(P_copy, 1)))
    for node in P_copy.difference((graph.neighbors(pivot))):
        for r in bk_pivot(graph, P.intersection(graph.neighbors(node)),
                          R=R.union(set([node])), X=X.intersection(graph.neighbors(node))):
            yield r
        P.remove(node)
        X.add(node)


def bk_order(graph, P, R=set(), X=set()):
    bk_order.count += 1
    for node in P.copy():
        for r in bk_order(graph, P.intersection(graph.neighbors(node)),
                          R=R.union(set([node])), X=X.intersection(graph.neighbors(node))):
            yield r
        P.remove(node)
        X.add(node)


if __name__ == '__main__':
    max_cliques = []

    R = nx.empty_graph()
    X = nx.empty_graph()
    P = nx.Graph()

    P.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (2, 5), (3, 4),
                      (4, 5), (4, 6), (5, 7), (5, 8), (7, 8)])
    graph = nx.Graph()
    graph.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (2, 5), (3, 4),
                          (4, 5), (4, 6), (5, 7), (5, 8), (7, 8)])
    # complement P
    # print(BK(R, P, X))
    bk.count = 0
    print("Bron-Kerbosch Backtracking:")
    for max_clique in bk(graph, set(graph.nodes)):
        print(max_clique)

    bk_pivot.count = 0
    print("Bron-Kerbosch Pivot:")
    for max_clique in bk_pivot(graph, set(graph.nodes)):
        print(max_clique)

    bk_order.count = 0
    print("Bron-Kerbosch Order:")
    for max_clique in bk_order(graph, set(nx.algorithms.coloring.strategy_largest_first(graph, 1))):
        print(max_clique)

# find max  of max_cliques (G.order?)
