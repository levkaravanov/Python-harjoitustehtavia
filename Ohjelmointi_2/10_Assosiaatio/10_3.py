class Hissi:
    def __init__(self, hissin_numero, alin_kerros, ylin_kerros):
        self.hissin_numero = hissin_numero
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros

    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros > self.ylin_kerros:
            print(f"❌ Tämä hissi ei voi nousta kerrokseen {kohde_kerros}")
        elif kohde_kerros < self.alin_kerros:
            print(f"❌ Hissi ei voi laskeutua alemmas kuin kerros {self.alin_kerros}")
        else:
            if kohde_kerros > self.kerros:
                while self.kerros < kohde_kerros:
                    self.kerros_ylös()
            else:
                while self.kerros > kohde_kerros:
                    self.kerros_alas()
            print(f"✅ Hissi {self.hissin_numero} pysähtyi kerrokseen {self.kerros}.")

    def kerros_ylös(self):
        self.kerros += 1
        print(f"⬆️ Hissi {self.hissin_numero} meni ylös kerrokseen {self.kerros}.")

    def kerros_alas(self):
        self.kerros -= 1
        print(f"⬇️ Hissi {self.hissin_numero} meni alas kerrokseen {self.kerros}.")

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_määrä):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissien_määrä = hissien_määrä
        self.hissit = []

        for i in range(hissien_määrä):
            hissin_numero = i + 1
            hissi = Hissi(hissin_numero, self.alin_kerros, self.ylin_kerros)
            self.hissit.append(hissi)

    def aja_hissiä(self, hissin_numero, kohdekerros):
        if 1 <= hissin_numero <= self.hissien_määrä:
            hissi = self.hissit[hissin_numero - 1]
            hissi.siirry_kerrokseen(kohdekerros)
        else:
            print(f"❌ Talossa ei ole hissiä {hissin_numero}")

    def palohälytys(self):
        print("🔥🔥🔥 Palohälytys! Kaikki hissit siirtyvät pohjakerrokseen! 🔥🔥🔥")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin_kerros)

t = Talo(3, 20, 10)

t.aja_hissiä(2, 5)
t.aja_hissiä(3, 5)
t.aja_hissiä(1, 10)
t.aja_hissiä(4, 5)
t.aja_hissiä(5, 9)
t.aja_hissiä(6, 7)


t.palohälytys()