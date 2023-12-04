from sys import getsizeof
import decimal
from ATM import ATM
from math import sqrt

def task1():
    a, b, c, d, e, f, g = "Hello world", 2, 2.5, [], (), {}, set()
    for item in (a, b, c, d, e, f, g):
        print(item, type(item))


def task2():
    data = [1, "hello_world", 2.5, 1, 5.5]
    for i, item in enumerate(data, start=1):
        print(i, item, getsizeof(item), hash(item), isinstance(item, int),
              isinstance(item, str))


def task3():
    number: int = int(input("Введите число: "))
    print(trans(number, 2), trans(number, 8))
    print(bin(number), oct(number))


def trans(num: int | float, n: int) -> int:
    result = []
    while num:
        # print(f"{num} % {n} = {num % n}")
        result.append(num % n)
        num //= n
    return sum(result[i] * 10 ** i for i in range(len(result)))
    # result = [str(item) for item in result[::-1]]
    # return int("".join(result))


def task4():
    decimal.getcontext().prec = 42
    diameter = decimal.Decimal(input("Введите диаметр: "))
    pi = decimal.Decimal('3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375')
    print("Длина окружности равна", pi * diameter)
    print("Площадь окружности равна", pi * (diameter / 2) ** 2)


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


def task6():
    atm = ATM()
    while True:
        print(atm)
        print("Введите от 1 до 3")
        print("1 - Пополнить счет")
        print("2 - Снять со счета")
        print("3 - Выйти")
        choice = input()
        match choice:
            case "1":
                print(atm.put_money(int(input("Введите сумму на которую вы хотите пополнить счет: "))))
            case "2":
                print(atm.take_money(int(input("Введите сумму снятия: "))))
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
