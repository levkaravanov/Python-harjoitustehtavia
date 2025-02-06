import random

def noppa(i):
    return random.randint(1, i)

tahko = int(input("Anna nopan tahkojen yhteismäärä: "))

if tahko < 3:
    print("Nopan tahkojen määrän täytyy olla vähintään 3.")
else:
    luku = 0
    while luku != tahko:
        luku = noppa(tahko)
        print(luku)