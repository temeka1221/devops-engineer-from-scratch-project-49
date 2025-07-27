"""Arithmetic progression game.

Генерирует прогрессию длинной от 5 до 15, скрывает одно число
И предлагает игроку его угадать.
"""

import random

from brain_games.games.constants import OPERAND_MAX, OPERAND_MIN

DESCRIPTION = "What number is missing in the progression?"
PROGRESSION_MIN_LENGTH = 5
PROGRESSION_MAX_LENGTH = 15
PROGRESSION_MIN_STEP = 2
PROGRESSION_MAX_STEP = 10
MISSED_INDEX_MIN = 0


def generate_round() -> tuple[str, str]:
    """
    Генерирует прогрессию и правильный ответ.

    :return:
        question: строка с прогрессией, где число заменено на ".."
        correct: скрытое число
    """
    length = random.randint(PROGRESSION_MIN_LENGTH, PROGRESSION_MAX_LENGTH)
    start = random.randint(OPERAND_MIN, OPERAND_MAX)
    step = random.randint(PROGRESSION_MIN_STEP, PROGRESSION_MAX_STEP)

    sequence = list(range(start, start + length * step, step))
    missed = random.randint(MISSED_INDEX_MIN, length - 1)

    correct = sequence[missed]
    question = " ".join(
        ".." if num == correct else str(num)
        for num in sequence
    )
    return question, str(correct)
