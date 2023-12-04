from sys import getsizeof
import decimal
from math import pi, sqrt


money_in_atm = decimal.Decimal()
count_operation = 0

def task1():
    a, b, c, d, e, f, g = "Hello world", 2, 2.5, [], (), {}, set()
    for item in (a, b, c, d, e, f, g):
        print(item, type(item))


# 2) Объедините студентов в команды по 2-5 человек  в сессионных залах.
# Создайте в переменной data список значений разных типов перечислив их через запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
# ●	порядковый номер начиная с единицы
# ●	значение
# ●	адрес в памяти
# ●	размер в памяти
# ●	хэш объекта
# ●	результат проверки на целое число только если он положительный
# ●	результат проверки на строку только если он положительный
# *Добавьте в список повторяющиеся элементы и сравните на результаты.

20


def task2():
    data = [1, "hello_world", 2.5, 1]
    result = []
    for i, item in enumerate(data, start=1):
        # print(("", "Строковое", "числовое")[isinstance(item, str) - isinstance(item, int)], item)
        print(i, item, id(item), getsizeof(item), hash(item), isinstance(item, int), isinstance(item, str),
              item in result)
        result.append(item)


# Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата.
# *Дополнительно
# ●	Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# ●	Избегайте магических чисел
# ●	Добавьте аннотацию типов где это возможно


def task3():
    DEAFULTNUMBER = "237"
    BIN, OCT, HEX = 2, 8, 16
    number: int = int(input("Введите число ") or DEAFULTNUMBER)
    print(bin(number), oct(number), hex(number))
    print(convert_to(number, BIN), convert_to(number, OCT), convert_to(number, HEX))


def convert_to(number, base, upper=False):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits):
        return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result.upper() if upper else result

def task4():
    decimal.getcontext().prec = 42
    diameter = decimal.Decimal(input("Введите диаметр: "))
    PI = decimal.Decimal(pi)
    print("Длина окружности равна", PI * diameter)
    print("Площадь окружности равна", PI * (diameter / 2) ** 2)


# Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.
# Используйте комплексные числа для извлечения квадратного корня.
# D>0 — уравнение имеет 2 корня: x 1 = (-b+√D)/2a, x 2 = (-b-√D)/2a. D=0 — уравнение имеет 1 корень: x = (-b)/2a. D<0 — уравнение не имеет корней.
def task5():
    a, b, c = int(input("Введите а: ")), int(input("Введите b: ")), int(input("Введите с: "))
    d = b ** 2 - 4 * a * c
    if d > 0:
        print((-1 * b - sqrt(d)) / (2 * a))
        print((-1 * b + sqrt(d)) / (2 * a))
    elif d == 0:
        print(-1 * (b / (2 * a)))
    else:
        d = complex(d, 0)
        print("Complex sqrt", (-1 * b - d ** 0.5) / (2 * a))
        print("Complex sqrt", (-1 * b + d ** 0.5) / (2 * a))


def tax():
    global money_in_atm
    if money_in_atm > 5_000_000:
        money_in_atm *= decimal.Decimal(0.9)
        print("Налог 10% при сумме более 5_000_000 у.е.")


def is_multiple_of_50(value):
    return value % 50 == 0


def count_increase():
    global count_operation
    count_operation += 1
    if not count_operation % 3:
        global money_in_atm
        money_in_atm *= decimal.Decimal(1.03)
        print("Начисление 3%")


def put_money(value):
    tax()
    global money_in_atm
    if is_multiple_of_50(value):
        money_in_atm += value
        count_increase()
        return f"Счет пополнен на {value} у.е."
    else:
        return "Можно пополнять на сумму кратную 50"


def take_money(value):
    tax()
    TAXFORTAKEMONEY = 1.5
    global money_in_atm
    if is_multiple_of_50(value):
        if money_in_atm > value:
            commission = decimal.Decimal(value * 0.015)
            if commission < 30:
                commission = 30
            else:
                commission = 600
            # t = value / 100 * TAXFORTAKEMONEY
            money_in_atm -= value +  commission
            count_increase()
            return f"Вы сняли {value} у.е. Налог на снятие {commission:.2f}"

        else:
            return "На Вашем счету не достаточно средств"
    else:
        return "Можно снять сумму кратную 50"


def task6():

    while True:
        print(f"На Вашем счету {money_in_atm:.2f} у.е.")
        print("Введите от 1 до 3")
        print("1 - Пополнить счет")
        print("2 - Снять со счета")
        print("3 - Выйти")
        choice = input()
        match choice:
            case "1":
                print(put_money(int(input("Введите сумму на которую вы хотите пополнить счет: "))))
            case "2":
                print(take_money(int(input("Введите сумму снятия: "))))
            case "3":
                break
            case _:
                print("Введено не верное значение")


def main():
    # task1()
    # task2()
    task3()
    # task4()
    # task5()
    # task6()


if __name__ == "__main__":
    main()
