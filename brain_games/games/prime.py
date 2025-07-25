"""Prime number game.

Генерирует число и предлагает угадать простое ли оно.
"""

import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num: int) -> bool:
    """
    Проверяет, является ли число простым.
    :param num: int
    :return:
        True or False
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0:
        return False

    limit = int(num ** 0.5)
    i = 3
    while i <= limit:
        if num % i == 0:
            return False
        i += 2
    return True


def generate_round() -> tuple[str, str]:
    """
    Генерирует случайное число и верный ответ
    :return:
        question: число в виде строки
        correct: "yes" если простое, иначе "no"
    """
    question = random.randint(1, 1000)
    correct = "yes" if is_prime(question) else "no"
    return str(question), correct
