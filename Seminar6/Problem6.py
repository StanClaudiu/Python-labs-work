import re

regex = "([ ][aeiouAEIOU][a-zA-Z]*[aeiouAEIOU])|^([aeiouAEIOU][a-zA-Z]*[aeiouAEIOU])"
input = "Acesta mesaj ar trebuii sa fie aici cenzurat. Acolo ar trebuii imediiiiiaaaa"

def censorshipLine(word):
    word = str(word.group(0)) # aici imi da propiu zis "match-ul"
    myWordList = []
    length = len(word)
    for index in range(0,length):
        if index % 2 == 1:
            myWordList.append("*")
        else :
            myWordList.append(word[index])
    return "".join(myWordList)



def censor(regex,input):
    return re.sub(regex,censorshipLine,input)

print(censor(regex,input))