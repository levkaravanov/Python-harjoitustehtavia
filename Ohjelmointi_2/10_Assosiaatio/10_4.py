import random
from tabulate import tabulate


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.matka = 0

    def kiihdytä(self, nopeus):
        uusi_nopeus = self.tämänhetkinen_nopeus + nopeus
        if uusi_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.tämänhetkinen_nopeus = 0
        else:
            self.tämänhetkinen_nopeus = uusi_nopeus

    def kulje(self, aika):
        self.matka += self.tämänhetkinen_nopeus * aika


class Kilpailu:
    def __init__(self, nimi, pituus_km, autot):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeusmuutos = random.randint(-10, 15)  # Случайное изменение скорости
            auto.kiihdytä(nopeusmuutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        data = [[auto.rekisteritunnus, auto.huippunopeus, auto.tämänhetkinen_nopeus, auto.matka] for auto in self.autot]
        headers = ["Rekisteritunnus", "Huippunopeus (km/h)", "Nopeus nyt (km/h)", "Matka (km)"]
        print("\n🚗 KILPAILUN TILANNE 🚗\n")
        print(tabulate(data, headers=headers, tablefmt="grid"))

    def kilpailu_ohi(self):
        return any(auto.matka >= self.pituus_km for auto in self.autot)

    def aja_kilpailu(self):
        tunti = 0
        while not self.kilpailu_ohi():
            self.tunti_kuluu()
            tunti += 1

            if tunti % 10 == 0 or self.kilpailu_ohi():
                self.tulosta_tilanne()

        voittaja = max(self.autot, key=lambda auto: auto.matka)
        print("\n🏁 KILPAILU ON PÄÄTTYNYT! 🏁\n")
        print(f"🥇 Voittaja: Auto {voittaja.rekisteritunnus}!")
        print(f"Huippunopeus: {voittaja.huippunopeus} km/h")
        print(f"Kokonaismatka: {voittaja.matka:.2f} km\n")


autot = [Auto(f"ABC-{i+1}", random.randint(100, 200)) for i in range(10)]

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)
kilpailu.aja_kilpailu()