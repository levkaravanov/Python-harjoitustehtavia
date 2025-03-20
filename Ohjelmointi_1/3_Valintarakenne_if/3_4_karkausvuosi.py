vuosi = int(input("Anna vuosi muodossa YYYY: "))
if vuosi > 0:
    if vuosi % 4 == 0 and (vuosi % 100 != 0 or vuosi % 400 == 0):
        print(f"{vuosi} on karkausvuosi")
    else:
        print(f"{vuosi} ei ole karkausvuosi")
else:
    print("Vuosi ei voi olla negatiivinen luku.")