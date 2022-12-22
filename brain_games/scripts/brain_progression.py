#!/usr/bin/env python3
from brain_games.games import brain_progression
from brain_games import engine


def main():
    engine.logic(brain_progression.game, brain_progression.games)


if __name__ == "__main__":
    main()
