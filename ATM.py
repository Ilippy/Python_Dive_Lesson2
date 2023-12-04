from decimal import Decimal


class ATM:
    MULTIPLICITY = 50
    PERCENT_REMOVAL = Decimal('1.5')
    MIN_REMOVAL = Decimal('30')
    MAX_REMOVAL = Decimal('600')
    RICHNESS_SUM = Decimal('5_000_000')
    RICHNESS_PERCENT = Decimal('10')
    COUNTER4PERCENTAGES = 3
    PERCENT_DEPOSIT = Decimal('3')

    def __init__(self):
        self.__money = Decimal()
        self.__count = 0

    def __is_multiple_of_50(self, value: int | float) -> bool:
        return value % self.MULTIPLICITY == 0

    def put_money(self, value: int) -> str:
        self.__tax()
        if self.__is_multiple_of_50(value):
            self.__money += value
            self.__count_increase()
            return f"Счет пополнен на {value} у.е."
        else:
            return f"Можно пополнять на сумму кратную {self.MULTIPLICITY}"

    def __tax(self):
        if self.__money >= self.RICHNESS_SUM:
            percent = self.__money / Decimal('100') * self.RICHNESS_PERCENT
            self.__money -= percent
            print(f"Налог {self.RICHNESS_PERCENT}% при сумме более {self.RICHNESS_SUM} составил {percent} у.е.")

    def __count_increase(self):
        self.__count += 1
        if not self.__count % self.COUNTER4PERCENTAGES:
            percent = self.__money / Decimal('100') * self.PERCENT_DEPOSIT
            self.__money += percent
            print(f"Начисление {self.PERCENT_DEPOSIT}% - {percent:.2f}")

    def take_money(self, value) -> Decimal | str:
        self.__tax()
        if self.__is_multiple_of_50(value):
            if self.__money > value:
                percent = value * self.PERCENT_REMOVAL
                percent = self.MIN_REMOVAL if percent < self.MIN_REMOVAL else self.MAX_REMOVAL if percent > self.MAX_REMOVAL else percent
                self.__money -= percent + value
                self.__count_increase()
                return f'Снятие с карты {value} у.е. Процент за снятие {percent:.2f} у.е.'
            else:
                return "На Вашем счету не достаточно средств"
        else:
            return f"Можно снять сумму кратную {self.MULTIPLICITY}"

    def __str__(self):
        return f"На Вашем счету {self.__money:.2f} у.е."
