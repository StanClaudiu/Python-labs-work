import re

regex = "50[0-9]{10}|12[0-9]{10}" # etc

reCompiled = re.compile(regex)
input = "121112223334"
def validateCNP(input):
    global reCompiled
    if reCompiled.match(input):
        return True
    return False
print(validateCNP(input))