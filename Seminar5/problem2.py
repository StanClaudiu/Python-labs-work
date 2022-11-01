def mySummer(*restOfThem,c,d) :
    return c + d

lamdaSummer = lambda *x,y,z : y + z 

if __name__ == "__main__" :
    print(mySummer(10,20,30, c =3, d =5))
    print(lamdaSummer(1,2,3,4,5,y =3,z =5))