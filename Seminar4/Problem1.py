import os
path = input("Give path : ")
myList = []

def myExtensionFinder(path) : 
    for(root,directories,files) in os.walk(path) :
        for fileName in files : 
            myExtension = os.path.splitext(fileName)[1]
            if myExtension != "" :
                myList.append(str(myExtension[1:]))
    myList.sort()
    return myList

print(myExtensionFinder(path))
