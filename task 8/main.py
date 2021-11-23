from itertools import product


def num_grid(input_data: list) -> list:
    """Функция принимает двумерную матрицу в виде списка списков, содержащую
     символы "#" и "-". Возвращает матрицу того же размера, что и исходная, в
      которой каждый символ  "-" заменен цифрой, обозначающей количество "#",
      непосредственно примыкающих к нему (по горизонтали, вертикали и диагоналям).

      Args:
          input_data: Двумерный список, все внутренние списки одинаковой длины и
           содержат только символы "#" или "-".

      Returns:
          Двумерный список того же размера, что и исходный, в котором каждый символ
        "-" заменен цифрой, обозначающей количество "#", непосредственно примыкающих к нему.

      Raises:
          ValueError: Входной список пуст.
          ValueError: Один из элементов входного списка не является списком.
          ValueError: Внутренние списки имеют разный размер.
          ValueError: Хотя бы в одном элементе матрицы имеется символ отлиный от '#' или '-'.
    """

    if len(input_data) == 0:
        raise ValueError('Недопустимый формат входных данных. Входной список пуст.')
    for i in input_data:
        if not isinstance(i, list):
            raise ValueError('Недопустимый формат входных данных, должен быть двумерный список.')
        if not len(i) == len(input_data[0]):
            raise ValueError('Недопустимый формат входных данных, все внутренние списки должны быть одинаковой длины.')

    nrows = len(input_data)
    ncolumns = len(input_data[0])

    result_lst = [[0] * ncolumns for _ in range(nrows)]

    for r, c in product(range(nrows), range(ncolumns)):
        if input_data[r][c] == '-':
            for i in range(max(0, r - 1), min(r + 2, nrows)):
                for j in range(max(0, c - 1), min(c + 2, ncolumns)):
                    result_lst[r][c] += 1 if input_data[i][j] == '#' else 0
            result_lst[r][c] = str(result_lst[r][c])
        elif input_data[r][c] == '#':
            result_lst[r][c] = '#'
        else:
            raise ValueError('Недопустимый формат входных данных. Один из символов отличен от # или -')
    return result_lst


assert (num_grid([[]]) == [[]])
assert (num_grid([['-']]) == [['0']])
assert (num_grid([['#']]) == [['#']])

assert (num_grid(
    [
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"]
    ]) == [
            ['0', '0', '0', '0', '0'],
            ['0', '1', '1', '1', '0'],
            ['0', '1', '#', '1', '0'],
            ['0', '1', '1', '1', '0'],
            ['0', '0', '0', '0', '0'],
        ])

assert (num_grid([
    ['-', '-', '-', '-', '#'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '#', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ["#", "-", "-", "-", "-"]
]) == [
            ['0', '0', '0', '1', '#'],
            ['0', '1', '1', '2', '1'],
            ['0', '1', '#', '1', '0'],
            ['1', '2', '1', '1', '0'],
            ['#', '1', '0', '0', '0']
        ])

assert (num_grid([
    ['-', '-', '-', '#', '#'],
    ['-', '#', '-', '-', '-'],
    ['-', '-', '#', '-', '-'],
    ['-', '#', '#', '-', '-'],
    ['-', '-', '-', '-', '-']
]) == [
            ['1', '1', '2', '#', '#'],
            ['1', '#', '3', '3', '2'],
            ['2', '4', '#', '2', '0'],
            ['1', '#', '#', '2', '0'],
            ['1', '2', '2', '1', '0'],
        ])