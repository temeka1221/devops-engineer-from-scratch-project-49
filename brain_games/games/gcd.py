"""GCD game.

Генерирует два случайных числа и предлагает найти их НОД.
"""

import math
import random

from brain_games.games.constants import OPERAND_MAX, OPERAND_MIN

DESCRIPTION = "Find the greatest common divisor of given numbers."


def generate_round() -> tuple[str, str]:
    """
    Генерирует пару случайных чисел и возвращает вопрос и верный ответ.
    :return:
        question: строка "a b"
        correct: строка, содержащая НОД "a b"
    """
    a = random.randint(OPERAND_MIN, OPERAND_MAX)
    b = random.randint(OPERAND_MIN, OPERAND_MAX)
    question = f"{a} {b}"
    correct = math.gcd(a, b)
    return question, str(correct)
