#!/usr/bin/env python3


#import brain_games.games.brain_even
#import brain_games.engine


#def main():
 #   print(brain_games.engine.action(brain_games.games.brain_even))


#if __name__ == '__main__':
  #  main()


import brain_games.games.brain_even
import brain_games.engine_copy


def main():
    brain_games.engine_copy.begin(brain_games.games.brain_even)


if __name__ == '__main__':
    main()
