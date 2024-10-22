def chill(wyr):
    gleb = 0
    maxgleb = 0

    for sign in wyr:
        if sign == '[':
            gleb += 1
            mexgleb = max(maxgleb, gleb)
        elif sign == ']':
            gleb -= 1
            if gleb < 0:
                return "Nah"

    if gleb != 0:
        return "nuh uh"


    return f"yuh uh max glebokosc too {maxgleb}"

wyr = input("podaj wyrarzenie")
fin = chill(wyr)
print(fin)
