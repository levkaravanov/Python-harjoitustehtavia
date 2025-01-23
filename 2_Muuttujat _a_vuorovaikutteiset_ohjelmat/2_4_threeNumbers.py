import math
import statistics

number1 = float(input("1. Anna luku: "))
number2 = float(input("2. Anna luku: "))
number3 = float(input("3. Anna luku: "))
numbers = [number1, number2, number3]
numbers_sum = sum(numbers)
numbers_product = math.prod(numbers)
numbers_average = round(statistics.mean(numbers), 2)

print(f"Lukujen summa on {numbers_sum}, tulo on {numbers_product} ja keskiarvo on {numbers_average}.")