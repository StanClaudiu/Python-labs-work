import os

def saveAllPaths(director, fisier) :
    try:
        fd = open(fisier,mode = "w")
        for(route,directory,files) in os.walk(director) :
           for file in files :  
            if str(file) != "" and file[0] == "P" :
                fd.write(str(route) + "\\" +str(file) + "\n")
    except Exception as e:
        print('Something went wrong' + e)
        if not fd.closed :
            fd.close()
    else : 
        fd.close()

saveAllPaths('../.','AllMyProblems.txt')