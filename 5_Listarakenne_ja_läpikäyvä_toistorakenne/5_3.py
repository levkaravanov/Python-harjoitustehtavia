luku = int(input("Anna kokonaisluku: "))

if luku < 2:
    print("Luku ei ole alkuluku.")
else:
    alkuluku = True
    for i in range (2, int(luku ** 0.5) + 1):
        if luku % i == 0:
            alkuluku = False
            break

    if alkuluku:
        print("Luku on alkuluku.")
    else:
        print("Luku ei ole alkuluku.")