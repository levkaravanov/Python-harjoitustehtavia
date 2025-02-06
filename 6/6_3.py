def gallona(i):
    return i * 3.785

print("Ohjelma muuntaa gallonat litroiksi. Syötä negatiivinen luku lopettaaksesi.")

while True:
    gal = float(input("Syötä gallonamäärä: "))
    if gal < 0:
        break
    print(f"{gal} gallonaa = {gallona(gal):.2f} litraa")