def doAllOperations(*sets):
    length = len(sets)
    totalCombinations = []
    for index in range(0,length) :
        for nextIndex in range(index + 1,length):
            firstSet = sets[index]
            secondSet = sets[nextIndex]
            mapper = dict()
            unionName = str(firstSet) + " | " + str(secondSet)
            intersectName = str(firstSet) + " & " + str(secondSet)
            minusFirstSecond = str(firstSet) + " - " + str(secondSet)
            minusSecondFirst = str(secondSet) + " - " + str(firstSet)
            mapper.setdefault(unionName,firstSet | secondSet)
            mapper.setdefault(intersectName,firstSet & secondSet)
            mapper.setdefault(minusFirstSecond,firstSet - secondSet)
            mapper.setdefault(minusSecondFirst,secondSet - firstSet)
            totalCombinations.append(mapper)
    return totalCombinations

print(doAllOperations({1,2}, {2, 3}))
            
