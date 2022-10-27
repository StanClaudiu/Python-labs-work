import os

def fileFinderGivenPath(path) :
    myFiles = []
    for(root,directories,files) in os.walk(path) :
        for file in files :
            myFiles.append(os.path.abspath(file))
    return myFiles

print(fileFinderGivenPath("../../"))