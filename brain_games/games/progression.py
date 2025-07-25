"""Arithmetic progression game.

Генерирует прогрессию длинной от 5 до 15, скрывает одно число
И предлагает игроку его угадать.
"""

import random

DESCRIPTION = "What number is missing in the progression?"


def generate_round() -> tuple[str, str]:
    """
    Генерирует прогрессию и правильный ответ.

    :return:
        question: строка с прогрессией, где число заменено на ".."
        correct: скрытое число
    """
    length = random.randint(5, 15)
    start = random.randint(1, 100)
    step = random.randint(2, 10)

    sequence = list(range(start, start + length * step, step))
    missed = random.randint(0, length - 1)

    correct = sequence[missed]
    question = " ".join(
        ".." if num == correct else str(num)
        for num in sequence
    )
    return question, str(correct)
