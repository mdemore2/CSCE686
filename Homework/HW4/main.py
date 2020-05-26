import networkx as nx
import numpy as np
import matplotlib


def BK(R, P, X):
    if nx.is_empty(nx.union(P, X)):
        return R
    #for vertex in P:
        #BK(nx.intersection(P, P.neighbors(vertex), nx.union(R, vertex), nx.intersection(X, P.neighbors(vertex))))
        #P_prime = P
        #P_neigh = P.neighbors(vertex)
        #for node in P_prime.nodes:
         #   for neighbor in P.neighbors(vertex):
                #if(node != )

        #R_prime = R
        #R_prime.add_node(vertex)
        #X_prime = nx.intersection(X,P.neighbors(vertex))
        #max_cliques.append(BK(R_prime,P_prime,X_prime))
        #P = P.remove_node(vertex)
        #X = nx.union(X, vertex)

def bronk(graph, P, R=set(), X=set()):
    '''
    Implementation of Bron–Kerbosch algorithm for finding all maximal cliques in graph
    '''
    if not any((P, X)):
        yield R
    for node in P.copy():
        for r in bronk(graph, P.intersection(graph.neighbors(node)),
                       R=R.union(node), X=X.intersection(graph.neighbors(node))):
            yield r
        P.remove(node)
        X.add(node)

def BK_pivot(R, P, X):
    return


def BK_order(G):
    return


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
    #complement P
    #print(BK(R, P, X))

    for max_clique in bronk(graph, set(graph.nodes)):
        print(max_clique)

    #find max  of max_cliques (G.order?)
