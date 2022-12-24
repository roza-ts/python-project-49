import brain_games.engine
from brain_games.games.brain_calc import question, result


def main():
    """Runs game"""
    brain_games.engine.game(question(), result(), result(), result())
    
    
if __name__ == '__main__':
    main()

