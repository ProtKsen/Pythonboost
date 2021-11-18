from constants import SIZE_OF_CELLS
import turtle


def turtle_settings(new_turtle: turtle.Turtle(), x_curr: int, y_curr: int) -> None:
    """
    Настройки "черепашки" для анимации, помещает ее в ячейку с координатами (x_curr, y_curr)
    """
    new_turtle.hideturtle()
    new_turtle.up()
    new_turtle.goto((x_curr + 1 / 2) * SIZE_OF_CELLS, -1 * (y_curr + 1 / 2) * SIZE_OF_CELLS)
    new_turtle.shape("turtle")
    new_turtle.speed('slowest')
    new_turtle.color('black')
    new_turtle.showturtle()
    new_turtle.down()


def screen_settings(screen: turtle.Screen()) -> None:
    """
    Настройки экрана анимации
    """
    screen.title("A Turtle in Labyrinth")
    screen.setworldcoordinates(-5, -10 * SIZE_OF_CELLS, 10 * SIZE_OF_CELLS, 5)
    turtle.TurtleScreen._RUNNING = True