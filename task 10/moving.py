import turtle
from itertools import product
from constants import SIZE_OF_CELLS
from settings import turtle_settings


def find_possible_steps(coord_x: int, coord_y: int, past_points: list, data: list) -> list:
    """
    Ищет координаты ячеек лабиринта, в которые можно двигаться после ячейки с координатами (coord_x, coord_y)

    Args:
        coord_x, coord_y: координаты точки, для которой выполняется поиск дальнейших шагов
        past_points: координаты ячеек, которые были пройдены ранее
        data: список, представляющий лабиринт

    Returns:
        Список коортежей с координатами ячеек лабиринта, куда можно идти дальше

    """
    height, weight = len(data), len(data[0])
    result_list = []
    for delta_x, delta_y in product(range(-1, 2), range(-1, 2)):
        if (
                0 <= coord_x + delta_x <= weight - 1 and
                0 <= coord_y + delta_y <= height - 1 and
                abs(delta_x * delta_y) != 1 and
                data[coord_y + delta_y][coord_x + delta_x] == 0 and
                (coord_x + delta_x, coord_y + delta_y) not in past_points
        ):
            result_list.append((coord_x + delta_x, coord_y + delta_y))
    return result_list


def find_way_in_labyrinth(x_curr: int, y_curr: int, x_prev: int, y_prev: int, x_stop: int, y_stop: int,
                          data: list, screen: turtle.Screen(), past_points: list) -> bool:
    """
        Поиск пути в лабиринте от ячейки (x_curr, y_curr) до ячейки (x_stop, y_stop).

        Args:
            x_curr, y_curr: координаты ячейки, с которой начинается поиск пути
            x_prev, y_prev: координаты ячейки, в которой указатель на шаг ранее, нужны для красивой анимации
            x_stop, y_stop: координаты последней ячейки
            data: список, представляющий лабиринт
            screen: экран анимации
            past_points: координаты ячеек, которые были пройдены ранее


        Returns:
            True - если проход есть, False - если прохода нет

        """
    if (x_curr, y_curr) not in past_points:
        new_turtle = turtle.Turtle()
        past_points.append((x_curr, y_curr))
        turtle_settings(new_turtle, x_prev, y_prev)
        new_turtle.goto((x_curr + 1 / 2) * SIZE_OF_CELLS, -1 * (y_curr + 1 / 2) * SIZE_OF_CELLS)
        stop_search = False
        while stop_search is False:
            next_points = find_possible_steps(x_curr, y_curr, past_points, data)
            if (x_stop, y_stop) in next_points:
                new_turtle.goto((x_stop + 1 / 2) * SIZE_OF_CELLS,
                                -1 * (y_stop + 1 / 2) * SIZE_OF_CELLS)
                new_turtle.color('green')
                return True
            if len(next_points) == 1:
                x_curr, y_curr = next_points[0][0], next_points[0][1]
                past_points.append((x_curr, y_curr))
                new_turtle.goto((x_curr + 1 / 2) * SIZE_OF_CELLS, -1 * (y_curr + 1 / 2) * SIZE_OF_CELLS)
            elif len(next_points) == 0:
                new_turtle.color('red')
                return False
            else:
                results = []
                for i in reversed(next_points):
                    new_turtle.hideturtle()
                    res = find_way_in_labyrinth(i[0], i[1], x_curr, y_curr, x_stop, y_stop, data, screen, past_points)
                    results.append(res)
                stop_search = True
        return True in results
    return False
