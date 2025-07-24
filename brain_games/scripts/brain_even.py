from random import randint

import prompt


def welcome_user() -> str:
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def print_rules() -> None:
    print('Answer "yes" if the number is even, otherwise "no".')


def is_even(num: int) -> bool:
    return num % 2 == 0


def make_question() -> tuple[int, str]:
    question = randint(1, 100)
    correct = "yes" if is_even(question) else "no"
    return question, correct


def ask_question(question: int) -> str:
    print(f"Question: {question}")
    return prompt.string("Your answer: ").strip().lower()


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print_rules()

    for _ in range(3):
        number, correct = make_question()
        answer = ask_question(number)
        if answer != correct:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct}'."
            )
            print(f"Let's try again, {name}!")
            return
        print("Correct!")

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    print("brain-even\n")
    main()
