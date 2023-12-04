def convert_to(number, base, upper=False):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits):
        return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result.upper() if upper else result


num = 0
# Введите ваше решение ниже
# print("Шестнадцатеричное представление числа:", hex(num)[2:].upper() if num else "")
print("Шестнадцатеричное представление числа:", convert_to(num, 16, True))
print("Проверка результата:", hex(num))
