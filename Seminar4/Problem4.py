import os
path = input("Give path bitte : ")
myList = [ file for file in os.listdir(path) if os.path.isfile(file)]
myExtensions = [ os.path.splitext(file)[1][1:] for file in myList]
mySet = set(myExtensions)
myExt = list(mySet)
myExt.sort()
print(myExt)