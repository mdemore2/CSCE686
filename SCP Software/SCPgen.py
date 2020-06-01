import random
import networkx as nx

def createSCP(paramsIN):
    graphSize = paramsIN[0]
    maxConnections = paramsIN[1]
    minConnections = paramsIN[2]
    costMin = paramsIN[3]
    costMax = paramsIN[4]

    sequenceList = []
    while not nx.is_graphical(sequenceList) or len(sequenceList) == 0:
        sequenceList = []
        for seqCount in range(0, graphSize):
                sequenceList.append(random.randint(minConnections, maxConnections))
    graph = nx.random_degree_sequence_graph(sequenceList, tries = 20)

    graph = graph.to_directed()
    adjList = nx.generate_adjlist(graph)

    totalSet = []
    totalSet.extend(range(0, graphSize))

    subsets = []
    for line in adjList:
        neighbors = list(map(int, line.split()[1:]))
        subsetCost = random.randint(costMin, costMax)
        tempItem = [neighbors, subsetCost]
        subsets.append(tempItem)

    return totalSet, subsets

def writeSCP(totalSetIn, subsetsIn, fileNameIn):
    setCoverStr = []
    setCoverStr.append("{{ {0} }}".format(" ".join(map(str, totalSetIn))))
    setCoverStr.append("")
    setCoverStr.append("{")
    for subset in subsetsIn:
        setCoverStr.append("  ({{ {0} }},{1})".format(" ".join(map(str,subset[0])), subset[1]))

    setCoverStr.append("}")

    with open(fileNameIn, 'w') as outFile:
        for line in setCoverStr:
            outFile.write(line +"\n")
