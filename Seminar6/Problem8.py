import re
import os
fileName = "./.."
regex = "^[^aeiouAEIOU].*\.py"


def findMatchyFiles(regex,string,fileName):
    rCompiled = re.compile(regex)
    for (root,directories,files) in os.walk(fileName) :
        for fileName in files:
            if rCompiled.match(fileName) and fileName.find(string)!=-1:
                print(" >> " + fileName)
            elif rCompiled.match(fileName) :
                print(fileName)
                



findMatchyFiles(regex,"1",fileName)
