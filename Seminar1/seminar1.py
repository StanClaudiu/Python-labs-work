#Exercitiul 1

def findCmmdc2Numbers(a,b) : 
    if a == 0 and b == 0 :
        return -1
    elif b == 0 :
        return a
    return findCmmdc2Numbers(b,a % b)


def findAllGcd() :
    myList = input()
    myList = "".join([number for number in myList if '0' <= number <= '9' or number == ','])
    myList = myList.split(',')
    myNumbers = []
    for numberString in myList :
        myNumbers.append(int(numberString))
    myGcd = myNumbers[0]
    for number in myNumbers : 
        myGcd = findCmmdc2Numbers(myGcd,number)
    return myGcd


#Exercitiul 2

def countVowels(string) : 
    return len([vowel for vowel in string if vowel in "aeiouAEIOU"])


#Exercitiul 3

def findApp(string1,string2) :
    if string1.find(string2) == -1 :
        return "",0
    occ = string1.find(string2)
    return (string1[:occ] +"#" +string1[occ+1 : ],1)
    
def getNumberOcc(string1, string2) : 
    counter = 0
    string1 , teller = findApp(string1,string2)
    while(teller != 0) :
        counter += 1
        string1,teller = findApp(string1,string2)
    else :
        return counter

print(getNumberOcc("bunaababa","aba"))

#Exercitiul 4

def replaceCaps(string) : 
    return "".join([ "_"+char if 'A' <= char <= 'Z' else char for char in string])[1:].lower()

print(replaceCaps("BunaZiuaToataLumea"))    

#Exercitiul 5

test = ["firs","n_lt","oba_","htyp"]

def spiralLoop(matrix) :
    size = len(matrix)
    up_left = (0,0)
    up_right = (0,size-1)
    down_left = (size-1,0)
    down_right = (size-1,size-1)
    determinedString = ""
    

#TO DO AS A HOMEWORK

#Exercitiul 6

def MakeReflect(number) :
    if (number % 10 == 0) :
        return -1
    returner = number % 10
    number = number // 10
    while ( number!= 0 ) :
        returner = 10* returner + number % 10
        number = number // 10
    return returner

def validatePalindrom(number) : 
    return MakeReflect(number) == number

#Exercitiul 7

def findFirstNumber(string) :
    numbers = [numb for numb in range(0,10)]
    min = 1000000000
    for number in numbers :
        if string.find(str(number)) >= 0 :
            if min > string.find(str(number)) :
                min = string.find(str(number))
    return min

def findFirst(string) : 
    pos = findFirstNumber(string)
    while '0' <= string[pos] <= '9' and pos < len(string) : #intentionat pus asa, se poate usor imbunatatii
        pos += 1
    else :
        return string[findFirstNumber(string):pos] 


print('The number is' + str(findFirst("abc100abc")))

#Exercitiul 8

def countBits(number) :
    if number % 2 == 1 :
        return 1 + countBits(number // 2)
    elif number == 0 :
        return 0
    return countBits(number // 2)

#Exercitiul 9

def mostCommonLetter(string) : 
    string = string.lower()
    string = "".join([ char for char in string if 'a'  <= char <= 'z' ])
    list_string = set(string)
    max = -1
    letter = -1
    for char in list_string :
        occ = string.count(char)
        if occ > max :
            max = occ
            letter = char
    return letter

#Homework to finish it!


print(mostCommonLetter('Asadar am auzit ca doresti sa vorbesti cu mine? Oooooooooooookay! '))

#Exercitiul 10

def countWords(text) : 
    withoutPunct = "".join([char for char in text if char == ' ' or 'a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9']) 
    return len(withoutPunct.split(' '))







print(countWords('Buna ziua, toata lumea!'))
print(countVowels('Rares'))
 