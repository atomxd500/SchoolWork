A = [2, -3, 1, -7, 4, -2, -1, 5, -3, 2, -1]

def wczytaj(plik):
    with open(plik,'r')as f:
        return[int(linia.strip()) for linia in f]

def najsuma_seg(tablica):
    maxsum = float('-inf')
    atksum = 0

    for liczba in tablica:
        aktsum += liczba
        if aktsum > maxsum:
            maxsum = aktsum
        if aktsum < 0:
            aktsum = 0

        return maxsum

tablica=wczytaj('dane1_3.txt')
end=najsuma_seg(tablica)
print("najwiekasza suma tablicy to ", end)
    
