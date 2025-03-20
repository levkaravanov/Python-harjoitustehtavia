"""Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
Ohjelma palauttaa listassa olevien lukujen summan.
Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan."""

def laskin(luvut):
    summa = 0
    for luku in luvut:
        summa += luku
    return summa

luvut = [1,32,2,3,4,5,6,7]

"""while True:
    luku = input("Syötä kokonaisluku (tyhjä lopettaa): ")
    if luku == "":
        break
    luvut.append(int(luku))
"""

print("Lukujen summa:", laskin(luvut))