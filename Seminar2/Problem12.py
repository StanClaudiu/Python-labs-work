def groupByRhyme(words) : 
    rhimes = list(map(lambda x : x[-2:],words))
    rhimes = set(rhimes)
    return [[word for word in words if word[-2:] == rhime] for rhime in rhimes]

print(groupByRhyme(['ana', 'banana', 'carte', 'arme', 'parte']))