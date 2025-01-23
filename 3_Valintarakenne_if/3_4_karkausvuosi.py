vuosi = int(input("Anna vuosi muodossa YYYY: "))
if vuosi > 0:
    if vuosi % 400 == 0:
        print(f"{vuosi} on karkausvuosi")
    elif vuosi % 4 == 0:
        if vuosi % 100 == 0 and vuosi % 400 == 0:
            print(f"{vuosi} on karkausvuosi")
        elif vuosi % 100 == 0 and vuosi % 400 != 0:
            print(f"{vuosi} ei ole karkausvuosi")
        else:
            print(f"{vuosi} on karkausvuosi")
    else:
        print(f"{vuosi} ei ole karkausvuosi")
else:
    print("Vuosi ei voi olla negatiivinen luku.")