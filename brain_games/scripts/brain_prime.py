#!/usr/bin/env python3
from brain_games.games import brain_prime
from brain_games import engine


def main():
    engine.start(brain_prime)


if __name__ == "__main__":
    main()
