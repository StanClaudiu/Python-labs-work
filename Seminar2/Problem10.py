def makeTuples(*lists) : 
    maxLength = max(list(map(lambda  x : len(x),lists)))
    return [[list[el] for list in lists ] for el in range(0,maxLength)]

print(makeTuples([1,2,3], [5,6,7], ["a", "b","c"]))