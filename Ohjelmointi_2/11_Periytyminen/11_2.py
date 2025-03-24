class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matkamittarilukema = 0.0

    def aseta_nopeus(self, nopeus):
        self.nopeus = nopeus

    def aja(self, tunnit):
        matka = self.nopeus * tunnit
        self.matkamittarilukema += matka


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko


# pääohjelma

sahkoauto = Sähköauto("ABC-15", 180, 52.5)
polttis = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.aseta_nopeus(100)
polttis.aseta_nopeus(95)

sahkoauto.aja(3)
polttis.aja(3)

print(f"Sähköauton {sahkoauto.rekisteritunnus} matkamittarilukema: {sahkoauto.matkamittarilukema} km")
print(f"Polttomoottoriauton {polttis.rekisteritunnus} matkamittarilukema: {polttis.matkamittarilukema} km")