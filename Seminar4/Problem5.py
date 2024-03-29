import os

def verifyForTarget(path,target) :
    if path[-10:].find(".") == -1 :
        return False # deoarece am eu niste fisiere de optimizare pe macos ce par sa fie doar niste hashuri
    buffer = ""
    try:
        fd = open(path,mode = "r")
        buffer = fd.read()
        fd.close()
    except:
        print(path)
        print("Something went wrong in verifyTarget ! ")
    return buffer.find(target) >= 0

def algorithmForGivenProb(path,target):
    myFoundFiles = []
    if not os.path.isdir(path) and not os.path.isfile(path) :
        raise Exception("Nu a fost introdus un path de director sau file")
    elif os.path.isdir(path):
        for(root,directory,files) in os.walk(path) :
         for file in files :
             if verifyForTarget(root + "/" + file,target) :
                myFoundFiles.append(root + "/" + file)
        return myFoundFiles
    return verifyForTarget(path,target) # case for a file

print(algorithmForGivenProb('/Users/claudiu-gavrilstan/Desktop/Anul3/Python/Python-labs-work','for'))