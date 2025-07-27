"""Calculator game: задает случайные выражения и проверяет ответы."""

import random
from operator import add, mul, sub

from brain_games.games.constants import OPERAND_MAX, OPERAND_MIN

DESCRIPTION = "What is the result of the expression?"
_OPERATIONS = {
    "+": add,
    "-": sub,
    "*": mul,
}


def generate_round() -> tuple[str, str]:
    """
    Генерирует одно арифметическое выражение и ответ к нему.

    :return:
        question: строка вида "a op b"
        correct: правильный ответ в виде строки
    """
    a = random.randint(OPERAND_MIN, OPERAND_MAX)
    b = random.randint(OPERAND_MIN, OPERAND_MAX)
    op = random.choice(list(_OPERATIONS))
    question = f"{a} {op} {b}"
    correct = _OPERATIONS[op](a, b)
    return question, str(correct)
