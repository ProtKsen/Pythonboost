def same_length(input_data: int) -> bool:
    """
    Метод принимает целое число и возвращает True, если в нем за каждой последовательностью единиц сразу же следует последовательность нулей той же длины.
    """
    input_data = str(input_data)
    while input_data.find('10') != -1:
        input_data = input_data.replace('10', '')
    return input_data.count('1') == 0


# мои тесты
assert (same_length(34573) is True)
assert (same_length(10345073) is True)
assert (same_length(11700) is False)

# тесты по условию
assert (same_length(110011100010) is True)
assert (same_length(101010110) is False)
assert (same_length(111100001100) is True)
assert (same_length(111) is False)
