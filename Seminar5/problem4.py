def getAllGoodDict(*dictionaries,dictionar = {},test ={}) :
    goodDict = []
    dictionaries = list(dictionaries)
    dictionaries.append(dictionar)
    dictionaries.append(test)
    for dict_ in dictionaries :
        if type(dict_) == dict :
            keySet = dict_.keys()
            if len(keySet) >= 2 :
             goodEnoughKey = False
             for key in keySet :
                if type(key) == str :
                    if len(key) >= 3 :
                        goodDict.append(dict_)
                        break
    return goodDict

print(getAllGoodDict( {1: 2, 3: 4, 5: 6}, 
 {'a': 5, 'b': 7, 'c': 'e'}, 
 {2: 3}, 
 [1, 2, 3],
 {'abc': 4, 'def': 5},
 3764,
 dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
 test={1: 1, 'test': True}))

