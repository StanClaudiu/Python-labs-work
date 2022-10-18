def getTupleUniqDup(list) :
    allElements = set(list)
    uniqElements = {elem for elem in allElements if list.count(elem) == 1}
    return (len(uniqElements),len(allElements - uniqElements))

print(getTupleUniqDup([1,1,1,1,2,2,2,2,3,4,5]))