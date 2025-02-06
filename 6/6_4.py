def laskin(luvut):
    return sum(luvut)

luvut = []

while True:
    luku = input("Syötä kokonaisluku (tyhjä lopettaa): ")
    if luku == "":
        break
    luvut.append(int(luku))

print("Lukujen summa:", laskin(luvut))