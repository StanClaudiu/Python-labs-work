def firstNFibboElem(n) :
    a = 0
    b = 1
    list = []
    while (n > 0) :
        list.append(a)
        c = b
        b = a + b
        a = c
        n = n - 1
    return list

print(firstNFibboElem(10))
