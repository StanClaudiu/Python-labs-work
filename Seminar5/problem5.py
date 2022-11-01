def getAllNumbers(givenList) :
    myNumbers = []
    for element in givenList :
        if type(element) == int or type(element) == float :
            myNumbers.append(element)
    return myNumbers

if __name__ == "__main__" :
    print(getAllNumbers([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))