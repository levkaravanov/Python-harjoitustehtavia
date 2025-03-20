"""Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy gallonamäärän
käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista
jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
Yksi gallona on 3,785 litraa."""

def gallona(i):
    return i * 3.785

print("Ohjelma muuntaa gallonat litroiksi. Syötä negatiivinen luku lopettaaksesi.")

while True:
    gal = float(input("Syötä gallonamäärä: "))
    if gal < 0:
        break
    print(f"{gal} gallonaa = {gallona(gal):.2f} litraa")