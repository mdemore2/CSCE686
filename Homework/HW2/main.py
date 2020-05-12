import time

#data input
test1 = [("Bob", 8, 9), ("Carl", 9, 10), ("Matt", 8.5, 9), ("John", 9.5, 10), ("Luke", 11, 12)]
test2 = [("Bob", 8, 9), ("Carl", 9, 10), ("Matt", 8.5, 9), ("John", 9.5, 10), ("Luke", 11, 12), ("Bob", 8, 9), ("Carl", 9, 10), ("Matt", 8.5, 9), ("John", 9.5, 10), ("Luke", 11, 12), ("Bob", 8, 9), ("Carl", 9, 10), ("Matt", 8.5, 9), ("John", 9.5, 10), ("Luke", 11, 12), ("Bob", 8, 9), ("Carl", 9, 10), ("Matt", 8.5, 9), ("John", 9.5, 10), ("Luke", 11, 12), ("Bob", 8, 9), ("Carl", 9, 10), ("Matt", 8.5, 9), ("John", 9.5, 10), ("Luke", 11, 12)]
test3 = [("Bob", 8, 9), ("Carl", 9, 10), ("Matt", 8.5, 9), ("John", 9.5, 10), ("Luke", 11, 12), ("Bob", 8, 9), ("Carl", 9, 10), ("Matt", 8.5, 9), ("John", 9.5, 10), ("Luke", 11, 12), ("Bob", 8, 9), ("Carl", 9, 10), ("Matt", 8.5, 9), ("John", 9.5, 10), ("Luke", 11, 12), ("Bob", 8, 9), ("Carl", 9, 10), ("Matt", 8.5, 9), ("John", 9.5, 10), ("Luke", 11, 12), ("Bob", 8, 9), ("Carl", 9, 10), ("Matt", 8.5, 9), ("John", 9.5, 10), ("Luke", 11, 12), ("Bob", 8, 9), ("Carl", 9, 10), ("Matt", 8.5, 9), ("John", 9.5, 10), ("Luke", 11, 12), ("Bob", 8, 9), ("Carl", 9, 10), ("Matt", 8.5, 9), ("John", 9.5, 10), ("Luke", 11, 12), ("Bob", 8, 9), ("Carl", 9, 10), ("Matt", 8.5, 9), ("John", 9.5, 10), ("Luke", 11, 12), ("Bob", 8, 9), ("Carl", 9, 10), ("Matt", 8.5, 9), ("John", 9.5, 10), ("Luke", 11, 12), ("Bob", 8, 9), ("Carl", 9, 10), ("Matt", 8.5, 9), ("John", 9.5, 10), ("Luke", 11, 12)]

CabOut = []
CabUse = []

def findCab(riderTime):
    index = 0 #cab number
    flag = False #do we need to add a cab
    for cab in CabUse:
        if (cab < riderTime[1]): #is one of the existing cabs available at this time
            cab = riderTime[2] #update next available time
            flag = True
            break
        index += 1
    if not flag:
        CabUse.append(riderTime[2]) #add new cab and update next available time
    return index

def assign(riderTime):
    cab = findCab(riderTime)
    CabStr = "Cab # " + str(cab)
    tup = (riderTime, CabStr)
    CabOut.append(tup) #data output: cab + rider pairings

def main():
    # MinCabGreedySearch
    t0 = time.clock()
    for item in test1:
        assign(item)
    t1 = time.clock() - t0
    print("TEST 1:")
    print("Input Size: " + str(len(test1)))
    print("Cabs Needed: " + str(len(CabUse)))
    print("Time Taken: " + str(t1))

    CabOut.clear()
    CabUse.clear()
    t2 = time.clock()
    for item in test2:
        assign(item)
    t3 = time.clock() - t2
    print("TEST 2:")
    print("Input Size: " + str(len(test2)))
    print("Cabs Needed: " + str(len(CabUse)))
    print("Time Taken: " + str(t3))

    CabOut.clear()
    CabUse.clear()
    t4 = time.clock()
    for item in test3:
        assign(item)
    t5 = time.clock() - t4
    print("TEST 2:")
    print("Input Size: " + str(len(test3)))
    print("Cabs Needed: " + str(len(CabUse)))
    print("Time Taken: " + str(t5))


if __name__ == "__main__":
    # execute only if run as a script
    main()

