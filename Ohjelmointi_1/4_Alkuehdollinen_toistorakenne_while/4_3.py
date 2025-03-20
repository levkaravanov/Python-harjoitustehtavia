numbers = []

while True:
    luku = input("Anna luku: ")
    if luku == "":
        break
    numbers.append(int(luku))

if numbers:
    print("Pienin luku on ", min(numbers))
    print("Suurin luku on", max(numbers))
else:
    print("Et antanut yhtään lukua.")
