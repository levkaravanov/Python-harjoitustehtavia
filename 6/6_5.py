"""Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin
parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut.
Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat
sen jälkeen sekä alkuperäisen että karsitun listan.
"""

def suodata_parilliset(lista):
    parilliset = []
    for i in lista:
        if i % 2 == 0:
            parilliset.append(i)
    return parilliset

alkuperainen_lista = []

while True:
    syote = input("Syötä kokonaisluku (tyhjä lopettaa): ")
    if syote == "":
        break
    alkuperainen_lista.append(int(syote))

print("Alkuperäinen lista:", alkuperainen_lista)
print("Parilliset luvut:", suodata_parilliset(alkuperainen_lista))