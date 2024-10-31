loan_amount = 1500000
win = 0
lose = 0
import random


arrest_chance = (-1 * (3.874 * (10 ** -11))*(loan_amount ** 2)) + (0.0001111 * loan_amount) + 18.87
#arrest_chance -= 4(luck)

if loan_amount >= 1434167:
    arrest_chance = 99

for i in range(100):
    if random.randint(0,100) <= arrest_chance:
        lose += 1
    else:
        win += 1

print(f"win: {win}\nlose: {lose}")
    