import re

input = "Buna ziua! Primiti cu colinda? Chiar daca este ora 16:00"

regex = ["[a-zA-Z]{4}","[a-z]{4}","[0-9]{2}:[0-9]{2}"]

def getAtLeastOnceMatchy(input,regexes):
    matchyWords = set()
    for regex in regexes :
        matchyWords |= set(re.findall(regex,input))
    return matchyWords

print(getAtLeastOnceMatchy(input,regex))