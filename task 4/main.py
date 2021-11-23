def is_pandigital(number):
    """
    Функция проверяет, является ли целое число,
    записанное в десятичной ситсеме, панцифровым
    """
    return len(set(str(number))) == 10


assert (is_pandigital(98140723568910) is True)
assert (is_pandigital(90864523148909) is False)
assert (is_pandigital(112233445566778899) is False)
