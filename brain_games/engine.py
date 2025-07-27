import prompt


def welcome_user() -> str:
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def ask_question(question: str) -> str:
    print(f"Question: {question}")
    return prompt.string("Your answer: ").strip().lower()


def run(game: callable, rounds: int = 3) -> None:
    name = welcome_user()
    print(game.DESCRIPTION)
    for _ in range(rounds):
        number, correct = game.generate_round()
        answer = ask_question(number)
        if answer != correct:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct}'."
            )
            print(f"Let's try again, {name}!")
            break
        print("Correct!")
    else:
        print(f"Congratulations, {name}!")
