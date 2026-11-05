n=int(input("entre le nombre n : "))
X=int(input("entre le nombre X : "))
P=1
for i in range(1,n+1) :
    P=1*(X**i)
print("X**n=",P)