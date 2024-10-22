def iloczyn(a):
    il=1
    for o in a:
        il=il*int(o)
    return str(il)

wczytany_napis=input("podaj liczbe")

ile=1
while len(iloczyn_liczb(wczytany_text))>1:

    wczytany_text=iloczyn_liczb(wczytany_text)
     
    ile+=1

print(ile)
   
