def myTupleMaker(numberList):
    evenList = []
    oddList = []
    for element in numberList :
        if element % 2 == 0 :
            evenList.append(element)
        if element % 2 == 1 :
            oddList.append(element)
    size = len(oddList)
    listTuples =[]
    for index in range(0,size) :
        listTuples.append((evenList[index],oddList[index]))
    return listTuples

print(myTupleMaker([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))
    
