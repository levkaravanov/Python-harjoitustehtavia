import random

nimet = set()

while True:
    nimi = input("Anna nimi: ")

    if nimi == "":
        break
    elif nimi not in nimet:
        nimet.add(nimi)
        print(f"{nimi} on uusi nimi")
    else:
        print("Aiemmin syötetty nimi")

nimet_lista = list(nimet)
random.shuffle(nimet_lista)

print("\nSyötetyt nimet satunnaisessa järjestyksessä:")
for nimi in nimet_lista:
    print(nimi)