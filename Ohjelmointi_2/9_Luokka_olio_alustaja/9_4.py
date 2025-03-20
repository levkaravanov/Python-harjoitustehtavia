"""Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi. Tee pääohjelman
alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä.
Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa.
Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

    - Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
    Tämä tehdään kutsumalla kiihdytä-metodia.
    -Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.

Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna."""
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

autot = []
for i in range(10):
    rekisteritunnus = f"ABC-{i+1}"
    huippunopeus = random.randint(100, 200)
    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)

race_finished = False
while True:
    for auto in autot:
        nopeus = random.randint(-10,15)
        auto.kiihdytä(nopeus)
        auto.kulje(1)
        if auto.matka >= 10000:
            voittaja = auto
            race_finished = True
            break
    if race_finished:
        break

data = [[auto.rekisteritunnus, auto.huippunopeus, auto.matka] for auto in autot]
headers = ["Rekisteritunnus", "Huippunopeus (km/h)", "Matka (km)"]

print("\n🏁 KILPAILUN TULOKSET 🏁\n")
print(tabulate(data, headers=headers, tablefmt="grid"))

print(f"\n🥇 Auto {voittaja.rekisteritunnus} on voittaja!")
print(f"Huippunopeus: {voittaja.huippunopeus} km/h")
print(f"Kokonaismatka: {voittaja.matka:.2f} km\n")