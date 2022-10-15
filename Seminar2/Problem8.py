

def fancyFunction(*lists,x = 1,flag = True) :
    print(lists)
    if flag :
        return [[ch for ch in el_list if ord(ch) % x == 0] for el_list in lists]
    return [[ch for ch in el_list if ord(ch) % x != 0] for el_list in lists]

print(fancyFunction("abc","bac","sdads", x = 1, flag = False))