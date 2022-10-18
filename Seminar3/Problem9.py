def testFunc(*myList,**aux):
    values = aux.values()
    values = [value for value in values]
    myList = list(set(myList))
    numberMatchyElements = len(list(filter(lambda el:el in values,myList)))
    return numberMatchyElements
print(testFunc(1, 2, 3, 4, x=1, y=2, z=3, w=5))