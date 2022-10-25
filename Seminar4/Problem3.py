from genericpath import isfile
import os
def myExtensionFinder(path) : 
    myList = []
    for(root,directories,files) in os.walk(path) :
        for fileName in files : 
            myExtension = os.path.splitext(fileName)[1]
            if myExtension != "" :
                myList.append(myExtension[1:])
    return myList

def myGetter(my_path) : 
    if os.path.exists(my_path) :
        if os.path.isfile(my_path) :
            try:
                fd = open(my_path,mode = "r")
                buffer = fd.read()
                print(buffer[-20:])
                return
            except Exception as e:
                print("Something went wrong:(" + str(e))
                fd.close()
            finally :
                fd.close()
        myExtensions = myExtensionFinder(my_path)
        myUnique = set(myExtensions)
        myList = [(myExt,myExtensions.count(myExt)) for myExt in myUnique]
        myList.sort(key = lambda x : x[1],reverse = True)
        return  myList

print(myGetter("."))
