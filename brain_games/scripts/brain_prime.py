#!/usr/bin/env python3


import brain_games.games.brain_prime
import brain_games.engine


def main():
    print(brain_games.engine.action(brain_games.games.brain_prime))


if __name__ == '__main__':
    main()
