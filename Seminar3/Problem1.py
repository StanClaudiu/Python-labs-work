from unittest import result


def getAllOperations(list1,list2) :
    set1 = set(list1)
    set2 = set(list2)
    resultList = []
    resultList.extend([set1.union(set2),set1.intersection(set2),set1.difference(set2),set2.difference(set1)])
    return resultList

print(getAllOperations([1,2,3,4],[3,4,5,6]))


