from decimal import Decimal


class ATM:
    TAXFORTAKEMONEY = Decimal('1.5')

    def __init__(self):
        self.__money = Decimal()
        self.__count = 0

    def __is_multiple_of_50(self, value: int | float) -> bool:
        return value % 50 == 0                                  #TODO избавиться от магический чисел

    def put_money(self, value: int) -> str:
        self.__tax()
        if self.__is_multiple_of_50(value):
            self.__money += value
            self.__count_increase()
            return f"Счет пополнен на {value} у.е."
        else:
            return "Можно пополнять на сумму кратную 50"        #TODO избавиться от магический чисел

    def __tax(self):
        if self.__money >= 5_000_000:                           #TODO избавиться от магический чисел
            self.__money *= 0.9                                 #TODO избавиться от магический чисел
            print("Налог 10% при сумме более 5_000_000 у.е.")   #TODO избавиться от магический чисел

    def __count_increase(self):
        self.__count += 1
        if not self.__count % 3:                                #TODO избавиться от магический чисел
            self.__money *= 1.03                                #TODO избавиться от магический чисел
            print("Начисление 3%")                              #TODO избавиться от магический чисел

    def take_money(self, value) -> Decimal | str:
        self.__tax()
        if self.__is_multiple_of_50(value):
            if self.__money > value:
                if 30 < value <= 600:                           #TODO избавиться от магический чисел
                    self.__money -= value
                    self.__count_increase()
                    return f"Вы сняли {value - value / 100 * self.TAXFORTAKEMONEY} у.е. Налог на снятие {self.TAXFORTAKEMONEY}"
                return "Вы можете снять в пределах 30..600"     #TODO избавиться от магический чисел
            else:
                return "На Вашем счету не достаточно средств"
        else:
            return "Можно снять сумму кратную 50"

    def __str__(self):
        return f"На Вашем счету {self.__money} у.е."
