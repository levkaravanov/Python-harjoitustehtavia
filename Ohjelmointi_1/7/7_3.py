lentoasemat = {}

while True:
    print("\nValitse toiminto:")
    print("1 - Lisää uusi lentoasema")
    print("2 - Hae lentoaseman tiedot")
    print("3 - Lopeta ohjelma")

    valinta = input("Anna valintasi (1-3): ")

    if valinta == "1":
        icao = input("Anna lentoaseman ICAO-koodi: ").upper()
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print(f"Lentoasema {nimi} ({icao}) lisätty.")

    elif valinta == "2":
        icao = input("Anna haettavan lentoaseman ICAO-koodi: ").upper()
        if icao in lentoasemat:
            print(f"Lentoasema: {lentoasemat[icao]}")
        else:
            print("Lentoasemaa ei löydy tietokannasta.")

    elif valinta == "3":
        print("Ohjelma päättyy.")
        break

    else:
        print("Virheellinen valinta, yritä uudelleen.")