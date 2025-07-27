"""Even or not even game: проверяет четность чисел"""

import random

from brain_games.games.constants import OPERAND_MAX, OPERAND_MIN

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num: int) -> bool:
    """
    Проверяет, является ли число четным.

    :param num: целое число
    :return:
        True, если число четное, иначе False
    """
    return num % 2 == 0


def generate_round() -> tuple[str, str]:
    """
    Генерирует случайное число и корректный ответ.

    :return:
        question: случайное число от 1 до 100
        correct: строку "yes" или "no" в зависимости от четности
    """
    question = random.randint(OPERAND_MIN, OPERAND_MAX)
    correct = "yes" if is_even(question) else "no"
    return str(question), correct
