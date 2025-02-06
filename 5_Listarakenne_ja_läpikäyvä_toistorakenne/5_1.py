import random

i = int(input("Kuinka monta arpakuutiota haluat heittää? Anna lukumäärä: "))

summa = 0

for _ in range(i):
    summa += random.randint(1,6)
print(summa)