def fibonacciList(index):
    c = 1
    b = 1
    a = 0
    myNumbers = []
    for rang in range(index) :
        c = a + b
        a = b
        b = c
        myNumbers.append(a)
    return myNumbers

print(fibonacciList(10))

def sum_digits(x):
    return sum(map(int, str(x)))

def myFibboHelper(filters = [lambda x : True], limit = 1000, offset = 0) :
    myNumbers = fibonacciList(1000) # now is done!
    for filter_ in filters :
        myNumbers = list(filter(filter_,myNumbers))
    return myNumbers [offset:offset + limit]

print(myFibboHelper([lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],2,2))