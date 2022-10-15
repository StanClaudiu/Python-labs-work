def primalityTest(x) :
    if x == 0 or x == 1 :
        return False
    if x == 2 :
        return True
    for index in range (2,x//2+1) :
        if x % index == 0 :
            return False
    return True
def getPrimeNumbers(List) :
    return list(filter(primalityTest,List))

print(getPrimeNumbers([1,2,3,4,5,6,7,8,9,10,11]))    