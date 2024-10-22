def iloczyn_liczb(a):
    iloczyn=1
    for liczba in a:
        iloczyn=int(liczba)
    return str(iloczyn)

moce=[]
min1=1000000000
max1=0








f=open('liczby.txt','r')
for x in f:
    x=x.strip()
    z=int(x)
    moc=0
    if len(x)>1:
        moc+=1
        x=iloczyn_liczb(x)
    if moc==1:
        
        if z>max1: max1=z
        else:
            if z<min1: min1=z
    moce.append(moc)

gg=max(moce)
for i in range(1,gg+1):
    y=moce.count(i)
    print(i,"\t",y)

print(min1,"\t",max1)










        
