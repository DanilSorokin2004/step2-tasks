# Напиши функцию is_palindrome(s), которая проверяет, является ли строка палиндромом (читается одинаково слева направо и справа налево).
# Функция возвращает True или False


def is_palindrome(string):
    return string == string[::-1]

# Проверки
print(is_palindrome('Dan'))       # False
print(is_palindrome('шалаш'))     # True
print(is_palindrome('123321'))    # True