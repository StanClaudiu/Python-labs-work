def makeVerification(word,pre,mid,end) :
    if(word.find(pre) != 0) :
        return False
    if (word.find(mid) == 0 and pre != "") or word.find(mid) == -1 :
        return False
    if (word.find(mid) == word.find(end) and end!="") or word.find(end) == -1:
        return False
    return True
        

def validate_dic (myDict,*rules) :
    keysPosible = set([ rule[0] for rule in rules])
    print(rules)
    print(myDict)
    print("Here are my rules : ",keysPosible)
    keysDict = set(myDict.keys())
    print(keysDict)
    if not keysDict <= keysPosible :
        return False
    for rule in rules :
        (key,pref,mid,end) = rule
        if key in keysDict :
            if not makeVerification(myDict[key],pref,mid,end) :
                return False
    return True
        
print(validate_dic({"key1": "come inside, it's too cold out", "key3": "this is not valid"},("key1", "", "inside", ""), ("key2", "start", "middle", "winter")))
