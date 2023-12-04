from fractions import Fraction

frac1 = "1/2"
frac2 = "1/3"

# Введите ваше решение ниже
a1, b1 = map(int, frac1.split("/"))
a2, b2 = map(int, frac2.split("/"))
print(f"Сумма дробей: {a1 * b2 + a2 * b1}/{b1 * b2}")
print(f"Произведение дробей: {a1 * a2}/{b1 * b2}")
f1, f2 = Fraction(frac1), Fraction(frac2)
print(f"Сумма дробей: {f1 + f2}")
print(f"Произведение дробей: {f1 * f2}")
