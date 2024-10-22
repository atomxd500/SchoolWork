#A = [-5,-8,9,3,-1,5,-3,6,-10]
f=open('dane1_3.txt','r')
A=readline(f)


n=len(A)

maxsum=max(A)
for dls in range(2,n+1):
    suma=sum(A[0:dls])
    print(suma, end="suma +-")
    for x in range(n-dls):
        suma=suma-A[x]+A[x+dls]
        print(suma)

        if suma>maxsum:
            maxsum=suma
            pr=A[x+1]
            ur=A[x+dls]
print('winiki koncowe',pr,ur, 'suma', maxsum)
