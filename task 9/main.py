def translator(input_str: str) -> str:
    """Функция переводит слово в виде обычного текста в «двуликий код».

      Args:
          input_str: строка, допускается написание как латиницей, так и кириллицей.

      Returns:
          строка, в которой слово «двуликий» используется для выражения слов в
           двоичном формате, заглавные буквы обозначают единицы, а строчные — нули.

      Raises:
          ValueError: Входные данные не являются строкой.
    """
    if not isinstance(input_str, str):
        raise ValueError('Недопустимый формат входных данных.')

    pattern = 'двуликий'
    result = ''
    for i in input_str:
        bytes_from_str = bytes(i, encoding='cp1251')
        int_from_bytes = int.from_bytes(bytes_from_str, 'big')
        bin_from_int = bin(int_from_bytes)[2:].zfill(8)
        res_lst = list(map(lambda x: x[0] if x[1] == '0' else x[0].upper(),
                           zip(pattern, bin_from_int)))
        result += ''.join(res_lst) + ' '
    return result.rstrip()


print(translator('абря'))

assert (translator("Hi") == "дВулИкий дВУлИкиЙ")
assert (translator("123") == "двУЛикиЙ двУЛикИй двУЛикИЙ")
