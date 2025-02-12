"""Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen
 yhteismäärän. Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
 Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan
  maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa."""

import random

def noppa(tahko_maara):
    return random.randint(1, tahko_maara)

tahko = int(input("Anna nopan tahkojen yhteismäärä: "))

if tahko < 3:
    print("Nopan tahkojen määrän täytyy olla vähintään 3.")
else:
    luku = 0
    while luku != tahko:
        luku = noppa(tahko)
        print(luku)