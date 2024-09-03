f=open('liczby.txt','r')
licznik=0
lista=f.readlines()
for bin in lista:
    if bin.count('0')>bin.count('1'):
        licznik+=1
       bin.strip('\n')
       if bin[-1]=='0':
           licz2+=1
           if bin[-3]=="000":
               licz8+=1
print(licznik)


print(licz2)
print(licz8)
