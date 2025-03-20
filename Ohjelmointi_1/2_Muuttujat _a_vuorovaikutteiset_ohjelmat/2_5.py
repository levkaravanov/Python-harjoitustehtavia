import math

leiviska = float(input("Anna leiviskät: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))

gramma = leiviska * 20 * 32 * 13.3 + naula * 32 * 13.3 + luoti * 13.3
kilogramma = math.floor(gramma / 1000)
gramma = round(gramma - kilogramma * 1000, 2)

print(f"Massa nykymittojen mukaan: {kilogramma} kilogrammaa ja {gramma} grammaa.")