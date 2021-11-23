from itertools import combinations_with_replacement
from collections import Counter

animals = ["dog", "cat", "bat", "cock", "cow", "pig", "fox", "ant", "bird", "lion", "wolf", "deer", "bear", "frog",
           "hen", "mole", "duck", "goat"]


def is_pattern_in_text(pattern: str, text: str) -> bool:
    """ Проверяет, можно ли из букв, входящих в text, составить строку pattern.

    Args:
      pattern: слово, которое нужно составить
      text: все доступные символы в виде одной строки

    Returns:
      True если успешно, False в обратном случае.

    """
    pattern = Counter(pattern)
    text = Counter(text)
    for i in pattern.keys():
        if pattern[i] > text.get(i, 0):
            return False
    return True


def count_animals(input_line: str) -> int:
    """ Принимает строку input_line и возвращает максимальное количество названий
          животных, которое возможно собрать из символов строки.

    Args:
      input_line: все доступные символы.

    Returns:
      Количество названий животных из animals, которое возможно собрать из символов строки input_line.

    """
    possible_words = set()
    for j in range(3, 5):
        for i in animals:
            if is_pattern_in_text(i, input_line):
                possible_words.add(i)
    for i in range(len(input_line) // 3, 0, -1):
        for j in combinations_with_replacement(possible_words, i):
            line = ''.join(j)
            if is_pattern_in_text(line, input_line):
                return i
    return 0


assert (count_animals("goatcode") == 2)
assert (count_animals("cockdogwdufrbir") == 4)
assert (count_animals("dogdogdogdogdog") == 5)
