def mineralFormation(input_list: list) -> str:
    """
    Функция определяет, представляет ли ввод (двухмерный список) сталактиты («stalactites»), сталагмиты («stalagmites»), и то, и другое («both»), или ни то, ни другое («None»).
    """
    if sum(input_list[0]) and sum(input_list[-1]):
        return 'both'
    elif sum(input_list[0]):
        return 'stalactites'
    elif sum(input_list[-1]):
        return 'stalagmites'
    return 'None'


assert (mineralFormation([
    [0, 1, 0, 1],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]) == "stalactites")

assert (mineralFormation([
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 1, 1, 1],
    [0, 1, 1, 1]
]) == "stalagmites")

assert (mineralFormation([
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [0, 1, 1, 1]
]) == "both")
