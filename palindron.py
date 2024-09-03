napis=input("podaj tekst a ja sprawdze czy to palindron")
napis=napis.replace(" ","")
odwr=(napis[::-1])
if napis ==odwr:
    print("to palindron")
else:
        print("to nie jest palindron")
