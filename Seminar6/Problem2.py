import re

input = "123 234 415 3020 Hallo Morgen"
regex = "([0-9]*)|[a-zA-Z]+"

def getNLengthMatches(string,regex,length):
    matches = []
    result = re.findall(regex,string)
    for elem in result :
        if len(elem) == length :
            matches.append(elem)
    return matches

print(getNLengthMatches(input,regex,3))

