def myEquals(dic1,dic2) :
    valKey1 = set(dic1)
    valKey2 = set(dic2)
    commonKeys = valKey1 & valKey2
    

print(myEquals({"a":1},{"b":2}))