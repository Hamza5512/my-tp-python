h=input("choisir une chaine de caractere :")
st=""
m=(h.lower())
for i in m :
    st=i+st

if m==st :
    print(h,"est un palindrome ")
else:
    print(h,"n'est pas un palindrome ")