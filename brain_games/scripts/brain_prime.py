#!/usr/bin/env python3
from brain_games.games import brain_prime
from brain_games import engine


def main():
    engine.logic(brain_prime.game, brain_prime.games)


if __name__ == "__main__":
    main()
