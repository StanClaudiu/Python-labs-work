from cmath import sqrt

def process_item(givenNumber) :
    if givenNumber < 2 :
        return 2
    good = True
    nextNumber = givenNumber
    while True  :
        good = True
        nextNumber = nextNumber + 1 
        for verify in range (2,nextNumber - 1):
            if nextNumber % verify == 0 :
                good = False
                break
        if good :
            return nextNumber

if  __name__ == "__main__" :
    number = input("Give a number : ")
    number = int(number)
    print(process_item(number))