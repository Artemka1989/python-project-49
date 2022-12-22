#!/usr/bin/env python3
from brain_games.games import brain_gcd
from brain_games import engine


def main():
    engine.logic(brain_gcd.game, brain_gcd.games)


if __name__ == "__main__":
    main()
