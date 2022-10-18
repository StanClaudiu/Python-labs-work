def getNumberAppDict(myString) : 
    setLetters = set(myString)
    return {letter:myString.count(letter) for letter in myString}

print(getNumberAppDict("Ana has apples."))