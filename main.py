from itertools import product
import turtle

SIZE_OF_CELLS = 17


def create_labyrinth(input_lst: list):
    height = len(input_lst)
    weight = len(input_lst[0])
    turtle.hideturtle()
    turtle.speed('fast')
    turtle.color('black')

    for i in range(height + 1):
        turtle.down()
        turtle.goto(weight * SIZE_OF_CELLS, -1 * i * SIZE_OF_CELLS)
        turtle.up()
        turtle.goto(0, -1 * (i + 1) * SIZE_OF_CELLS)
    turtle.up()
    turtle.goto(0, 0)
    for i in range(weight + 1):
        turtle.down()
        turtle.goto(i * SIZE_OF_CELLS, -1 * height * SIZE_OF_CELLS)
        turtle.up()
        turtle.goto((i + 1) * SIZE_OF_CELLS, 0)

    #for i, j in product(range(height), range(weight)):
    #    if input_lst[i][j] == 1:
    #        turtle.goto((j + 1 / 2) * SIZE_OF_CELLS, -1 * (i + 3 / 4) * SIZE_OF_CELLS)
    #        turtle.begin_fill()
    #        turtle.fillcolor('red')
    #        turtle.circle(SIZE_OF_CELLS / 4)
    #        turtle.end_fill()


def turtle_settings(new_turtle, x_prev, y_prev, x_curr, y_curr):
    new_turtle.up()
    new_turtle.goto((x_prev + 1 / 2) * SIZE_OF_CELLS, -1 * (y_prev + 1 / 2) * SIZE_OF_CELLS)
    new_turtle.shape("turtle")
    new_turtle.showturtle()
    new_turtle.speed('slowest')
    new_turtle.down()
    new_turtle.color('black')
    new_turtle.goto((x_curr + 1 / 2) * SIZE_OF_CELLS, -1 * (y_curr + 1 / 2) * SIZE_OF_CELLS)


def screen_settings(screen: turtle.Screen()):
    screen.title("A Turtle in Labyrinth")
    screen.setworldcoordinates(-5, -10 * SIZE_OF_CELLS, 10 * SIZE_OF_CELLS, 5)
    turtle.TurtleScreen._RUNNING = True


def find_possible_steps(coord_x, coord_y, height, weight, x_prev, y_prev, data):
    result = []
    for delta_x, delta_y in product(range(-1, 2), range(-1, 2)):
        if (
                0 <= coord_x + delta_x <= weight - 1 and
                0 <= coord_y + delta_y <= height - 1 and
                abs(delta_x * delta_y) != 1 and
                (delta_x != 0 or delta_y != 0) and
                data[coord_y + delta_y][coord_x + delta_x] == 0 and
                [coord_x + delta_x, coord_y + delta_y] != [x_prev, y_prev]
            ):
            result.append([coord_x + delta_x, coord_y + delta_y])
    return result


def try_to_find_way(x_curr, y_curr, x_prev, y_prev, x_stop, y_stop, data, screen):
    n, m = len(data), len(data[0])
    new_turtle = turtle.Turtle()
    turtle_settings(new_turtle, x_prev, y_prev, x_curr, y_curr)
    create_new_turtle = False
    while create_new_turtle is False:
        coords_next = find_possible_steps(x_curr, y_curr, n, m, x_prev, y_prev, data)
        if [x_stop, y_stop] in coords_next:
            new_turtle.goto((x_stop + 1 / 2) * SIZE_OF_CELLS,
                            -1 * (y_stop + 1 / 2) * SIZE_OF_CELLS)
            new_turtle.color('green')
            return True
        if len(coords_next) == 1:
            x_prev, y_prev = x_curr, y_curr
            x_curr, y_curr = coords_next[0][0], coords_next[0][1]
            coords_next.pop(0)
            new_turtle.goto((x_curr + 1 / 2) * SIZE_OF_CELLS, -1 * (y_curr + 1 / 2) * SIZE_OF_CELLS)
        elif len(coords_next) == 0:
            new_turtle.color('red')
            return
        else:
            for i in coords_next:
                try_to_find_way(i[0], i[1], x_curr, y_curr, x_stop, y_stop, data, screen)
                create_new_turtle = True
    return False


def can_exit(input_lst: list) -> bool:
    n, m = len(input_lst), len(input_lst[0])
    x_start, y_start = 0, 0
    x_stop, y_stop = m - 1, n - 1
    x_prev, y_prev = 0, 0
    if input_lst[y_start][x_start] == 1:
        return False
    else:
        screen = turtle.Screen()
        screen_settings(screen)
        create_labyrinth(input_lst)
        res = try_to_find_way(x_start, y_start, x_prev, y_prev, x_stop, y_stop, input_lst, screen)
        screen.exitonclick()
        print(res)
        return res


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
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
