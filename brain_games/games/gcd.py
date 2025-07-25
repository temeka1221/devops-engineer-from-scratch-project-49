"""GCD game.

Генерирует два случайных числа и предлагает найти их НОД.
"""

import math
import random

DESCRIPTION = "Find the greatest common divisor of given numbers."


def generate_round() -> tuple[str, str]:
    """
    Генерирует пару случайных чисел и возвращает вопрос и верный ответ.
    :return:
        question: строка "a b"
        correct: строка, содержащая НОД "a b"
    """
    a, b = random.randint(1, 100), random.randint(1, 100)
    question = f"{a} {b}"
    correct = math.gcd(a, b)
    return question, str(correct)
