import turtle
from itertools import product
from constants import SIZE_OF_CELLS


def draw_labyrinth(input_lst: list) -> None:
    """
    Рисует лабиринт, стены отмечены красными кружками (почему то очень долго рисуются( )

    Args:
        input_lst: список, представляющий лабиринт
    """
    height, width = len(input_lst), len(input_lst[0])
    turtle.hideturtle()
    turtle.speed('fast')
    turtle.color('black')

    for i in range(height + 1):
        turtle.down()
        turtle.goto(width * SIZE_OF_CELLS, -1 * i * SIZE_OF_CELLS)
        turtle.up()
        turtle.goto(0, -1 * (i + 1) * SIZE_OF_CELLS)
    turtle.up()
    turtle.goto(0, 0)
    for i in range(width + 1):
        turtle.down()
        turtle.goto(i * SIZE_OF_CELLS, -1 * height * SIZE_OF_CELLS)
        turtle.up()
        turtle.goto((i + 1) * SIZE_OF_CELLS, 0)

    for i, j in product(range(height), range(width)):
        if input_lst[i][j] == 1:
            turtle.goto((j + 1 / 2) * SIZE_OF_CELLS, -1 * (i + 3 / 4) * SIZE_OF_CELLS)
            turtle.begin_fill()
            turtle.fillcolor('red')
            turtle.circle(SIZE_OF_CELLS / 4)
            turtle.end_fill()
