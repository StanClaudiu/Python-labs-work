def sortTuples(*tuples):
    tuples = list(tuples)
    print(tuples)
    tuples.sort(key = lambda x : x[1][2])
    return tuples

print(sortTuples(('abc', 'bcd'), ('abc', 'zza')))