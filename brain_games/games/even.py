"""Even or not even game: проверяет четность чисел"""

import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise "no".'


def is_even(num: int) -> bool:
    """
    Проверяет, является ли число четным.

    :param num: целое число
    :return:
        True, если число четное, иначе False
    """
    return num % 2 == 0


def generate_round() -> tuple[int, str]:
    """
    Генерирует случайное число и корректный ответ.

    :return:
        question: случайное число от 1 до 100
        correct: строку "yes" или "no" в зависимости от четности
    """
    question = random.randint(1, 100)
    correct = "yes" if is_even(question) else "no"
    return question, correct
