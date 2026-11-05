S=0
N=int(input("choisir le nombre N : "))
if N>0 :
    for i in range(1,N+1) :
        S=S+(1/i)
    print("S=",S)
else:
    print("impossible de calculer S")