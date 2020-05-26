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
    else:
        P_copy = P.copy()
        pivot = random.choice(list(P.union(X)))
        #pivot = int(str(random.sample(P_copy, 1)))
        for node in P_copy.difference((graph.neighbors(pivot))):
            for r in bk_pivot(graph, P.intersection(graph.neighbors(node)),
                              R=R.union(set([node])), X=X.intersection(graph.neighbors(node))):
                yield r
            P.remove(node)
            X.add(node)



def bk_order_pivot(graph, P, R=set(), X=set()):
    bk_order_pivot.count += 1
    if not any((P, X)):
        yield R
    else:
        P_copy = P.copy()
        pivot = random.choice(list(P.union(X)))
        #pivot = int(str(random.sample(P_copy, 1)))
        for node in P_copy.difference((graph.neighbors(pivot))):
            for r in bk_order_pivot(graph, P.intersection(graph.neighbors(node)),
                              R=R.union(set([node])), X=X.intersection(graph.neighbors(node))):
                yield r
            P.remove(node)
            X.add(node)

def bk_order(graph, P, R=set(), X=set()):
    for node in P.copy():
        for r in bk_order_pivot(graph, P.intersection(graph.neighbors(node)),
                          R=R.union(set([node])), X=X.intersection(graph.neighbors(node))):
            yield r
        P.remove(node)
        X.add(node)


if __name__ == '__main__':

    graph = nx.Graph()
    graph.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (2, 5), (3, 4),
                          (4, 5), (4, 6), (5, 7), (5, 8), (7, 8)])

    graph = nx.complement(graph)

    bk.count = 0
    print("Bron-Kerbosch Backtracking:")
    for max_clique in bk(graph, set(graph.nodes)):
        print(max_clique)

    bk_pivot.count = 0
    print("Bron-Kerbosch Pivot:")
    for max_clique in bk_pivot(graph, set(graph.nodes)):
        print(max_clique)

    bk_order_pivot.count = 0
    print("Bron-Kerbosch Order:")
    for max_clique in bk_order(graph, set(nx.algorithms.coloring.strategy_largest_first(graph, 1))):
        print(max_clique)

