import random

number = random.randint(1,10)

print("Tervetuloa arvauspeliin!")
print("Tietokone on valinnut satunnaisen luvun väliltä 1–10. Yritä arvata se!")

while True:
    userNumber = int(input("Anna luku: "))
    if number == userNumber:
        print("Oikein! Onneksi olkoon!")
        break
    elif number < userNumber:
        print("Liian suuri arvaus, yritä uudestaan!")
    else:
        print("Liian pieni arvaus, yritä uudestaan!")