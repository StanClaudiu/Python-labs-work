def explicator(pairs) :
    myListOfDict = []
    for pair in pairs :
        first,second = pair
        myDict = {}
        myDict["sum"] = first + second
        myDict["prod"] = first * second
        myDict["pow"] = first ** second
        myListOfDict.append(myDict)
    return myListOfDict

print(explicator([(5, 2), (19, 1), (30, 6), (2, 2)] ))