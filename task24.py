from math import sin

x = int(input("Введите число x: "))

print(f"sin(3.2 + (1 - x)**0.5 / abs(5 * x)) \
      = {sin((3.2 + (1 - x)**0.5) / abs(5 * x))}")