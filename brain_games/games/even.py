from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise "no".'


def is_even(num: int) -> bool:
    return num % 2 == 0


def generate_round() -> tuple[int, str]:
    question = randint(1, 100)
    correct = "yes" if is_even(question) else "no"
    return question, correct
