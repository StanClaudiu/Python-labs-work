vowels = "AEIOUaeiou"

def filterMethod(word):
    myVowels = list(filter(lambda x : x in vowels,word))
    return myVowels

def secondMethod(word):
    return [chr for chr in word if chr in vowels]

def thirdMethod(word):
    myVowels = []
    for chr in word :
        if chr in vowels :
            myVowels.append(chr)
    return myVowels

if __name__ == "__main__" :
    print(filterMethod("Aici este frumos"))
    print(secondMethod("Aici este frumos"))
    print(thirdMethod("Aici este frumos"))