import os

def verifyForTarget(path,target,callback) :
    if path[-10:].find(".") == -1 :
        return False # deoarece am eu niste fisiere de optimizare pe macos ce par sa fie doar niste hashuri
    buffer = ""
    try:
        fd = open(path,mode = "r")
        buffer = fd.read()
        fd.close()
    except Exception as e:
        callback(e)
    return buffer.find(target) >= 0

def algorithmForGivenProb(path,target,callback):
    myFoundFiles = []
    if not os.path.isdir(path) and not os.path.isfile(path) :
        callback(Exception("Nu ati introdus un director sau file"))
    elif os.path.isdir(path):
        for(root,directory,files) in os.walk(path) :
         for file in files :
             if verifyForTarget(root + "/" + file,target,callback) :
                myFoundFiles.append(root + "/" + file)
        return myFoundFiles
    return verifyForTarget(path,target,callback) # case for a file

def callback(e):
    print("Our error is : " + str(e))

print(algorithmForGivenProb('/Users/claudiu-gavrilstan/Desktop/Anul3/Python/Python-labs-work','for',callback))