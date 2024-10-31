for i in range(1400000):
    arrest_chance = (-1 * (3.874 * (10 ** -11))*(i ** 2)) + (0.0001111 * i) + 18.87
    print(f"{int(arrest_chance)}: {i}")