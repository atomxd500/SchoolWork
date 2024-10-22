a=int(input("podaj liczbe naturalna"))

def czyn(n):
    ile=0
    p=3
    if n%2==0: return False
    while n>1:
        
        if n%p==0: ile+=1
        while n%p==0:
            n=n//p   
        p+=2
        if ile>3:return False

    if ile==3: return True
    if lie<3: return False
    
#p=2
#czyn=[]
#while a>1:
#    while a%p==0:
#       a=a//p
#        czyn.append(p)
#    if p>2: p+=2
#    else:
#        p+=1
print(czyn(a))
