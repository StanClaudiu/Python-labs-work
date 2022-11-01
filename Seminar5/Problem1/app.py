import utils

if __name__ == "__main__" :
    while True :
        givenNumber = input("Give a number : ")
        if givenNumber == "q" :
            exit(-1)
        givenNumber = int(givenNumber)
        print(utils.process_item(givenNumber))