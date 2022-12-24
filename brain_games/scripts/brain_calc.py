import brain_games.engine
from brain_games.games.brain_calc import task, result


def main():
    """Runs game"""
    brain_games.engine.game(task(), result(), result(), result())


if __name__ == '__main__':
    main()
