def setFunctions(list1,list2) : 
    listIntersect = [ elem1 for elem1 in list1 for elem2 in list2 if elem1 == elem2]
    list1minus2 = [elem1 for elem1 in list1 if elem1 not in list2]
    list2minus1 = [elem2 for elem2 in list2 if elem2 not in list1]
    listUnited = [elem for elem in listIntersect]
    listUnited.extend(list1minus2)
    listUnited.extend(list2minus1)
    return list1minus2,list2minus1,listIntersect,listUnited

print(setFunctions([1,2,3,4],[2,3,4,5,6]))