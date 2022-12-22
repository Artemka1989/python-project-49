#!/usr/bin/env python3
import random


game = "What is the result of the expression?"


def games():
    num = random.randint(1, 10)
    operator = random.choice('+-*')
    num_1 = random.randint(1, 10)
    question = f"Question: {num} {operator} {num_1}"
    if operator == "+":
        calc = num + num_1
    if operator == "-":
        calc = num - num_1
    if operator == "*":
        calc = num * num_1
    return question, calc
