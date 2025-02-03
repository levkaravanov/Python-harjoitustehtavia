luku = input("Anna luku: ")

if luku == "":
    print("Et antanut yhtään lukua.")
else:
    suurin = int(luku)
    pienin = int(luku)

    while True:
        luku = input("Anna luku: ")
        if luku == "":
            break
        luku = int(luku)

        if luku < pienin:
            pienin = luku
        elif luku > suurin:
            suurin = luku

    print(f"Pienin luku on {pienin}")
    print(f"Suurin luku on {suurin}")