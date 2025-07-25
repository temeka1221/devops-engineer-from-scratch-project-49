"""Calculator game: задает случайные выражения и проверяет ответы."""

import random
from operator import add, mul, sub

DESCRIPTION = "What is the result of the expression?"
_OPERATIONS = {
    "+": add,
    "-": sub,
    "*": mul,
}


def generate_round() -> tuple[str, str]:
    """
    Генерирует один раунд игры.
    :return:
        question= строка вида "a op b"
        correct= правильный ответ в виде строки
    """
    a, b = random.randint(1, 100), random.randint(1, 100)
    op = random.choice(list(_OPERATIONS))
    question = f"{a} {op} {b}"
    correct = _OPERATIONS[op](a, b)
    return question, str(correct)
