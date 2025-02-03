numbers = []

while True:
    luku = input("Anna luku: ")
    if luku == "":
        break
    numbers.append(int(luku))
numbers.sort(reverse=True)
if numbers:
    for x in numbers[:5]:
        print(x)
else:
    print("Et antanut yhtään lukua.")