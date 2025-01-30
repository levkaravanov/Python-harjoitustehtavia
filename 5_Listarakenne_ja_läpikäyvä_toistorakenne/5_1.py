import random

i = int(input("Kuinka monta arpakuutiota haluat heittää? Anna lukumäärä: "))

summa = 0

for _ in range(i):
    number = random.randint(1,6)
    summa += number

print(summa)