import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus = 0, matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = tämänhetkinen_nopeus
        self.matka = matka

    def kulje(self, aika):
        self.tämänhetkinen_nopeus = random.randint(0, self.huippunopeus)
        matka = self.tämänhetkinen_nopeus * aika
        self.matka += matka

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti, tämänhetkinen_nopeus = 0, matka=0):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus, tämänhetkinen_nopeus, matka)

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin, tämänhetkinen_nopeus =0, matka=0):
        self.bensatankin = bensatankin
        super().__init__(rekisteritunnus, huippunopeus, tämänhetkinen_nopeus, matka)

autot = []

autot.append(Polttomoottoriauto("ABC-123", 165, 32.3))
autot.append(Sähköauto("ABC-15", 180, 52.5))

for a in autot:
    a.kulje(3)
    print(a.matka)
    a.kulje(4)
    print(a.matka)