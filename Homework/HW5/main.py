import os
import random
import re
import subprocess
from statistics import mean
import timeit
import networkx as nx

# Regex’s to  find  solutions in  AFIT  SCP output
solutionRegEx = re.compile(r'TheuSolutionuSet:u\[((?:[0-9]+,\ s)*[0 -9]+) \]')
costRegEx = re.compile(r'Totalucost:u([0 -9]+)$')


# generic   wrapper   to   use   timeit   with   functions   that
#	require   arguments
def timeitWrapper(function, *args, **kwargs):
    def wrapped():
        return function(*args, **kwargs)

    return wrapped


# generic   function   that   returns   time   elapsed   of   timeit
def timeitFunction(repNum, function, *args, **kwargs):
    funcWrapper = timeitWrapper(function, *args, **kwargs)
    runTime = timeit.timeit(funcWrapper, number=repNum)
    return runTime


# Create   a   random   instance   of   our   problem   domain   based   on   parameters
# [0] -  Graph Size
# [1]  -  Max Degree
# [2]   -   Min   Degree
# [3]   -   cost   min
# [4]  -  cost max
def createSCP(paramsIn):
    graphSize = paramsIn[0]
    maxConnections = paramsIn[1]
    minConnections = paramsIn[2]
    costMin = paramsIn[3]
    costMax = paramsIn[4]

    # Generate   random   degree   sequence   and   make   sure   the   sequence   can   create   a   graph
    sequenceList = []
    while not nx.is_graphical(sequenceList) or len(sequenceList) == 0:
        sequenceList = []
    for seqCount in range(0, graphSize):
        sequenceList.append(random.randint(minConnections, maxConnections))
    graph = nx.random_degree_sequence_graph(sequenceList, tries=20)
    graph = graph.to_directed()
    adjList = nx.generate_adjlist(graph)

    # create total set  and  the  subsets
    totalSet = []
    totalSet.extend(range(0, graphSize))

    subsets = []
    for line in adjList:
        neighbors = list(map(int, line.split()[1:]))
        subsetCost = random.randint(costMin, costMax)
        tempItem = [neighbors, subsetCost]
        subsets.append(tempItem)

    return totalSet, subsets


# write   random   problem   into   AFIT   SCP   format
def writeSCP(totalSetIn, subsetsIn, fileNameIn):
    setCoverStr = []
    setCoverStr.append("{{ u {0} u}}".format(" u".join(map(str, totalSetIn))))
    setCoverStr.append("")
    setCoverStr.append("{")
    for subset in subsetsIn:
        setCoverStr.append(" uu ({{ u {0} u }} ,{1})".format(" u".join(map(str, subset[0])), subset[1]))
        setCoverStr.append("}")

        with   open(fileNameIn, 'w ') as outFile:
            for line in setCoverStr:
                outFile.write(line + '\n')

        # run  AFIT SCP


def runSCP(probFileName, resultFileName, programFileName):
    try:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        subprocess.check_output([" scp Problem . bat", dir_path, probFileName, resultFileName, programFileName])
    except subprocess.CalledProcessError:
        i = 0

        # find  results  in  AFIT  SCP output


def analyzeResults(resultFileName):
    dataDict = {}
    setList = []
    cost = 0

    solution = False

    with open(resultFileName, 'r') as fileIn:
        for line in fileIn:
            if not solution:
                solutionMatch = solutionRegEx.match(line)
                if solutionMatch:
                    solution = True
                    setList = list(map(int, solutionMatch.group(1).split(",u")))
            else:
                costMatch = costRegEx.match(line)
                if costMatch:
                    cost = int(costMatch.group(1))

    dataDict[" solution Set "] = setList
    dataDict[" dronesPicked "] = len(setList)
    dataDict[" cost"] = cost
    return dataDict

    # create   1   random   problem   and   solve   it   using   AFIT   SCP
    #	returns   data   from   AFIT   SCP


def testSCP(paramsIn):
    probFileName = " random SetCover . txt"
    resultFileName = " scp Result. txt"
    totalSet, subsets = createSCP(paramsIn)

    writeSCP(totalSet, subsets, probFileName)
    runData = {}
    programs = [" defaultSC PSolver . jar", " h 1 SCPSolver . jar", " h 2 SCPSolver . jar"]
    for program in programs:
        runTime = timeitFunction(1, runSCP, probFileName, program[0: -4] + resultFileName, program)
        dataDict = analyzeResults(program[0: -4] + resultFileName)
        dataDict[" run Time"] = runTime
        runData[program] = dataDict
    return runData

    # perform   multiple   iterations   of   testSCP
    # return  aggregate data


def repeatSCP(repeatNum, paramsIn):
    totalData = {}
    for testNum in range(0, repeatNum):
        testDict = testSCP(paramsIn)
        if testNum == 0:
            for key in testDict:
                totalData[key] = {}
                for subKey in testDict[key]:
                    totalData[key][subKey] = []
        for key in testDict:
            for subKey in testDict[key]:
                totalData[key][subKey].append(testDict[key][subKey])
    finalData = {}
    for key in totalData:
        finalData[key] = {}
        finalData[key][" avg D ronesPicked "] = mean(totalData[key][" dronesPicked "])
        finalData[key][" avg Cost"] = mean(totalData[key][" cost"])
        finalData[key][" avg Run Time "] = mean(totalData[key][" run Time"])
    return finalData


def updateStatus(printTxt):
    with open(" status. txt", 'w ') as outFile:
        outFile.write("{0} u Complete .\n".format(printTxt))

        # test cases

        # SCP   Parameters:
        #	Number   of   drones/ subsets ,   max   comm   links ,   min   comm   links


# if __name__ == "__main__":
small = [20, 5, 2, 1, 1]
medium = [40, 5, 2, 1, 1]
large = [60, 5, 2, 1, 1]
largeSparse = [60, 3, 1, 1, 1]
largeDense = [60, 6, 4, 1, 1]

print(" Small:")
print(repeatSCP(5, small))
updateStatus(" Small")

print(" Medium :")
print(repeatSCP(5, medium))
updateStatus(" Medium ")

print(" Largeu Sparse:")
print(repeatSCP(5, largeSparse))
updateStatus(" Largeu Sparse")

print(" Large:")
print(repeatSCP(5, large))
updateStatus(" Large")

print(" Largeu Dense:")
print(repeatSCP(5, largeDense))
updateStatus(" Largeu Dense")

weightedLarge = [60, 5, 2, 1, 10]
weightedLargeSparse = [60, 3, 1, 1, 10]
weightedLargeDense = [60, 6, 4, 1, 10]

print(" Weighted u Largeu Sparse:")
print(repeatSCP(5, weightedLargeSparse))
updateStatus(" Weighted u Largeu Sparse")

print(" Weighted u Large:")
print(repeatSCP(5, weightedLarge))
updateStatus(" Large")

print(" Weighted u Largeu Dense:")
print(repeatSCP(5, weightedLargeDense))
updateStatus(" Weighted u Largeu Dense")
