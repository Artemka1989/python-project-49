#!/usr/bin/env python3
from brain_games.games import brain_even
from brain_games import engine


def main():
    engine.logic(brain_even.game, brain_even.games)


if __name__ == "__main__":
    main()
