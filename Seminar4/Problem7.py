import os

def getAllInfo(path) :
    myDict = {}
    if os.path.exists(path) : 
        myDict.setdefault("fullPath",os.path.abspath(path))
        myDict.setdefault("file_size",os.path.getsize(path))
        if(os.path.splitext(path)[1] != "") :
            myDict.setdefault("file_extension,",os.path.splitext(path)[1][1:])
        myDict.setdefault("file_extension,", "\"\"" )
        myDict.setdefault("can_read",os.access(path,os.R_OK))
        myDict.setdefault("can_write",os.access(path,os.W_OK))
    return myDict

print(getAllInfo("Problem1.py"))