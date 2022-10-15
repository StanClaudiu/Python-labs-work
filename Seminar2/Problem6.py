def myCounter(howMany,*lists) : 
    megaUnion = set()
    bigList = []
    for list in lists :
        bigList.extend(list) 
    megaUnion = set(bigList)
    return len([elem for elem in megaUnion if bigList.count(elem) == 2])


print(myCounter(2,[1,2,3], [2,3,4],[4,5,6], [4,1, "test"]))