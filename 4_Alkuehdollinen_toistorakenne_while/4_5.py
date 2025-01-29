userId = "python"
password = "rules"

i=0

while i<5:
    inpUserId = input("Käyttäjätunnus: ")
    inpPassword = input("Salasana: ")

    if inpUserId == userId and inpPassword == password:
        print("Tervetuloa")
        break
    else:
        if i<5:
            print("Väärä käyttäjätunnus tai salasana. Yritä uudelleen.")
            i += 1
            if i<5:
                print(f"Yrityksiä jäljellä: {5 - i}/5.")
            else:
                print("Pääsy evätty")
                break