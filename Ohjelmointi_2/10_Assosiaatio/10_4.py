import random
from tabulate import tabulate


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
        elif uusi_nopeus < 0:
            self.tämänhetkinen_nopeus = 0
        else:
            self.tämänhetkinen_nopeus = uusi_nopeus

    def kulje(self, aika):
        matka = self.tämänhetkinen_nopeus * aika
        self.matka += matka

class Kilpailu:
    def __init__(self, nimi, kilometrimäärä, autonmäärä):
        self.nimi = nimi
        self.kilometrimäärä = kilometrimäärä
        self.autonmäärä = autonmäärä
        self.autot = []
        self.voittaja = None
        self.race_finished = False

        for i in range(self.autonmäärä):
            rekisteritunnus = f"ABC-{i + 1}"
            huippunopeus = random.randint(100, 200)
            auto = Auto(rekisteritunnus, huippunopeus)
            self.autot.append(auto)

    def tunti_kuluu(self, aika):
        for auto in self.autot:
            nopeus = random.randint(-10, 15)
            auto.kiihdytä(nopeus)
            auto.kulje(aika)


    def tulosta_tilanne(self):
        data = [[auto.rekisteritunnus, auto.huippunopeus, auto.matka] for auto in self.autot]
        headers = ["Rekisteritunnus", "Huippunopeus (km/h)", "Matka (km)"]
        print("\n🏁 KILPAILUN TULOKSET 🏁\n")
        print(tabulate(data, headers=headers, tablefmt="grid"))

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.kilometrimäärä:
                self.voittaja = max(self.autot, key=lambda x: x.matka)
                return True
        return False


k = Kilpailu("Suuri romuralli", 8000, 10)

tunti = 0
while not k.kilpailu_ohi():
    k.tunti_kuluu(1)
    tunti += 1
    if tunti % 10 == 0:
        k.tulosta_tilanne()

k.tulosta_tilanne()

voittaja = k.voittaja
print(f"\n🥇 Auto {voittaja.rekisteritunnus} on voittaja!")
print(f"Huippunopeus: {voittaja.huippunopeus} km/h")
print(f"Kokonaismatka: {voittaja.matka:.2f} km\n")