import random
from myfuzzer.Timer import Timer


def my_sqrt(x):
    """Computes the square root of x, using the Newton-Raphson method"""
    approx = None
    guess = x / 2
    while approx != guess:
        approx = guess
        guess = (approx + x / approx) / 2
    return approx


def assertEqualsEps(x, y, epsilon=1e-8):
    assert abs(x - y) < epsilon  # use math.isclose!


if __name__ == '__main__':
    assertEqualsEps(my_sqrt(4), 2)
