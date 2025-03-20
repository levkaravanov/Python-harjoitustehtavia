class Hissi:
    def __init__(self, alimman_kerros, ylimmän_kerros):
        self.alimman_kerros = alimman_kerros
        self.ylimmän_kerros = ylimmän_kerros
        self.kerros = alimman_kerros

    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros > self.ylimmän_kerros:
            print(f"❌ Tämä hissi ei voi nousta kerrokseen {kohde_kerros}")
        elif kohde_kerros < self.alimman_kerros:
            print(f"❌ Hissi ei voi laskeutua alemmas kuin kerros {self.alimman_kerros}")
        else:
            if kohde_kerros > self.kerros:
                while self.kerros < kohde_kerros:
                    self.kerros_ylös()
            else:
                while self.kerros > kohde_kerros:
                    self.kerros_alas()
            print(f"✅ Hissi pysähtyi kerrokseen {self.kerros}.")

    def kerros_ylös(self):
        self.kerros += 1
        print(f"⬆️ Hissi meni ylös kerrokseen {self.kerros}.")

    def kerros_alas(self):
        self.kerros -= 1
        print(f"⬇️ Hissi meni alas kerrokseen {self.kerros}.")


h = Hissi(1, 10)

h.siirry_kerrokseen(6)
h.siirry_kerrokseen(100)
h.siirry_kerrokseen(-1)
h.siirry_kerrokseen(-10)
h.siirry_kerrokseen(1)
h.siirry_kerrokseen(5)