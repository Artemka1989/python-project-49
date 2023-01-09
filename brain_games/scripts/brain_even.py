#!/usr/bin/env python3
from brain_games.games import brain_even
from brain_games import engine


def main():
    engine.start(brain_even)


if __name__ == "__main__":
    main()
