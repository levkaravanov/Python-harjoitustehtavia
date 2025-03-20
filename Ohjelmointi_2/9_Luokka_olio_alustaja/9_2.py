"""Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h).
Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h.
Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
Kuljettua matkaa ei tarvitse vielä päivittää."""


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus=0, matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = tämänhetkinen_nopeus
        self.matka = matka

    def kiihdytä(self, nopeus):
        uusi_nopeus = self.tämänhetkinen_nopeus + nopeus

        if uusi_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus
            print(f"Auto {self.rekisteritunnus} saavutti huippunopeuden {self.huippunopeus} km/h.")
        elif uusi_nopeus < 0:
            self.tämänhetkinen_nopeus = 0
            print(f"Auto {self.rekisteritunnus} hätäjarrutti ja pysähtyi.")
        else:
            self.tämänhetkinen_nopeus = uusi_nopeus
            print(f"Auto {self.rekisteritunnus} kiihdytti nopeuteen {self.tämänhetkinen_nopeus} km/h.")


auto1 = Auto("ABC-123", 142)

print(f"Auton rekisteritunnus: {auto1.rekisteritunnus}"
      f"\nhuippunopeus: {auto1.huippunopeus} km/h"
      f"\ntämänhetkinen nopeus: {auto1.tämänhetkinen_nopeus} km/h"
      f"\nmatka: {auto1.matka} km")

auto1.kiihdytä(30)
auto1.kiihdytä(70)
auto1.kiihdytä(50)
auto1.kiihdytä(-200)
