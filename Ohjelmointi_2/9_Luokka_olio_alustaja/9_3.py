"""Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa
kuljetun matkan lukemaan 2090 km."""


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

    def kulje(self, aika):
        matka = self.tämänhetkinen_nopeus * aika
        self.matka += matka
        print(f"Auto {self.rekisteritunnus} kulki {matka:.1f} km, kokonaismatka: {self.matka:.1f} km.")

auto1 = Auto("ABC-123", 142)

print(f"Auton rekisteritunnus: {auto1.rekisteritunnus}"
      f"\nhuippunopeus: {auto1.huippunopeus} km/h"
      f"\ntämänhetkinen nopeus: {auto1.tämänhetkinen_nopeus} km/h"
      f"\nmatka: {auto1.matka} km")

auto1.kiihdytä(30)
auto1.kulje(1.5)
auto1.kiihdytä(70)
auto1.kulje(1.5)
auto1.kiihdytä(50)
auto1.kulje(1.5)
auto1.kiihdytä(-200)
auto1.kulje(1.5)
