import turtle
from moving import find_way_in_labyrinth
from drawing import draw_labyrinth
from settings import screen_settings


def can_exit(input_lst: list) -> bool:
    """
    Определяет, можно ли пройти в лабиринте от первого до последнего элемента. Параллельно решение представлено в
    графическом виде, по завершении ждет клика мышки по экрану. Если нулевой элемент равен 1,
    то сразу возвращает False без рисунка.

    Args:
        input_lst: двумерный список, содержащий только нули и единицы, при этом единицы обозначают стены лабиринта,
        а нули - области, где можно двигаться.

    Returns:
        True - если проход есть, False - если прохода нет.
    """
    height, width = len(input_lst), len(input_lst[0])
    x_start, y_start = 0, 0
    x_stop, y_stop = width - 1, height - 1
    x_prev, y_prev = x_start, y_start
    if input_lst[y_start][x_start] == 1:
        return False
    screen = turtle.Screen()
    screen_settings(screen)
    draw_labyrinth(input_lst)
    has_way = find_way_in_labyrinth(x_start, y_start, x_prev, y_prev, x_stop, y_stop, input_lst, screen, [])
    screen.exitonclick()
    return has_way


if __name__ == '__main__':
    assert (can_exit([
        [0, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 0]
    ]) is True)

    assert (can_exit([
        [0, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0, 1, 1],
        [1, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 1, 0, 0, 1],
        [1, 1, 0, 0, 1, 1, 1]
    ]) is False)

    assert (can_exit([
        [0, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1]
    ]) is False)

    assert (can_exit([
        [0, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [1, 1, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 0]
    ]) is True)
