from brain_games import engine, games


def main():
    """Точка входа: запускает цикл игровых раундов через engine."""
    engine.run(games.even)


if __name__ == "__main__":
    main()
