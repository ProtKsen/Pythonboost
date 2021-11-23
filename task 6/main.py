def harry(input_arr: list, path=False) -> int:
    """
    Находит максимальную сумму элементов двумерного списка, которую можно
     получить двигаясь от элемента [0][0] до последнего элемента. На каждом
     шаге можно идти либо вправо, либо вниз.

    Время работы алгоритма O(n*m), где n,m - размерности списка.
    Параметр path определяет, нужно ли восстановить путь, дающий максимальную сумму.
    """
    # размерность входного массива
    n, m = len(input_arr), len(input_arr[0])

    # проверим предельные случаи
    if m == 0:  # если входной массив пуст
        return -1
    elif n == 1:  # если входной массив сдержит только одну строку
        if path:
            print('Последовательность значений: ', *input_arr)
            print('Последовательность координат: ', *[[0, i] for i in range(m)])
        return sum(*input_arr)
    elif m == 1:  # если вхондной массив содержит только один столбец
        if path:
            print('Последовательность значений: ', *[i[0] for i in input_arr])
            print('Последовательность координат: ', *[[i, 0] for i in range(n)])
        return sum([i[0] for i in input_arr])

    # Заведем массив max_sum того же размера, что и входной массив. В ячейке max_sum
    # с координатами [i][j] будем хранить максимальную сумму, которую можно получить,
    # двигась во входном массиве от элемента [0][0] до элемента [i][j].
    # Если нужно восстановить путь, создаем также массив для хранения направления движения
    max_sum = [[0] * m for _ in range(n)]
    if path:
        direction = [[''] * m for _ in range(n)]

    # для элемента [0][0] значение max_sum определяется однозначно
    max_sum[0][0] = input_arr[0][0]
    if path:
        direction[0][0] = 'start'

    # в элементы нулевого столбца можно попасть только двигась все время вниз
    for i in range(1, n):
        max_sum[i][0] = max_sum[i - 1][0] + input_arr[i][0]
        if path:
            direction[i][0] = 'down'

    # в элементы нулевой строки можно попасть, только двигясь всегда вправо
    for j in range(1, m):
        max_sum[0][j] = max_sum[0][j - 1] + input_arr[0][j]
        if path:
            direction[0][j] = 'right'

    # счетчики линий и столбцов
    curr_line, curr_col = 1, 1

    while curr_line < n or curr_col < m:
        # заполняем строку массива max_sum от [curr_line][1] до [curr_line][curr_col - 1]
        if curr_line < n:
            for j in range(1, curr_col):
                if max_sum[curr_line][j - 1] > max_sum[curr_line - 1][j]:
                    max_sum[curr_line][j] = max_sum[curr_line][j - 1] + input_arr[curr_line][j]
                    if path:
                        direction[curr_line][j] = 'right'
                else:
                    max_sum[curr_line][j] = max_sum[curr_line - 1][j] + input_arr[curr_line][j]
                    if path:
                        direction[curr_line][j] = 'down'

        # заполняем столбец массива max_sum от [1][curr_col] до [curr_line][curr_col]
        if curr_col < m:
            for i in range(1, min(n, curr_line + 1)):
                if max_sum[i][curr_col - 1] > max_sum[i - 1][curr_col]:
                    max_sum[i][curr_col] = max_sum[i][curr_col - 1] + input_arr[i][curr_col]
                    if path:
                        direction[i][curr_col] = 'right'
                else:
                    max_sum[i][curr_col] = max_sum[i - 1][curr_col] + input_arr[i][curr_col]
                    if path:
                        direction[i][curr_col] = 'down'

        # счетчик линии или столбца не должен превышать n и m соответственно
        curr_line = min(curr_line + 1, n)
        curr_col = min(curr_col + 1, m)

    # восстанавливаем путь
    if path:
        i, j = n - 1, m - 1
        res_coord = [[i, j]]
        res_val = [input_arr[i][j]]
        curr_dir = direction[i][j]
        while curr_dir != 'start':
            if curr_dir == 'right':
                i, j = i, j - 1
            elif curr_dir == 'down':
                i, j = i - 1, j
            res_coord.append([i, j])
            res_val.append(input_arr[i][j])
            curr_dir = direction[i][j]
        print('Последовательность значений: ', res_val[::-1])
        print('Последовательность координат: ', res_coord[::-1])

    return max_sum[-1][-1]


# тесты по условию
assert (harry([[5, 2], [5, 2]]) == 12)
assert (harry([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]) == 72)
assert (harry([[]]) == -1)

# мои примеры
print('Пример 1')
data = [[1, 2, 5]]
print('Входной массив:', data)
print('Максимальная сумма:', harry(data, path=True))
print('------------------------')

print('Пример 2')
data = [[1], [2], [5]]
print('Входной массив:', data)
print('Максимальная сумма:', harry(data, path=True))
print('------------------------')

print('Пример 3')
data = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 900, 10],
    [11, 12, 13, 14, 15]
]
print('Входной массив:', *data, sep='\n')
print('Максимальная сумма:', harry(data, path=True))
print('------------------------')
