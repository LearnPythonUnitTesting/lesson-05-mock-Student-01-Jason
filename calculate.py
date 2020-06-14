import random


def get_random():
    return random.random()


def get_int():
    r = get_random()
    if r > 0.5:
        return 1
    else:
        return 0
