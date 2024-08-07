import math


def assertEqualsTolerance(x, y, epsilon=1e-8):
    assert math.isclose(x, y, rel_tol=epsilon)  # abs(x - y) < epsilon


def my_sqrt(x):
    """Computes the square root of x, using the Newton-Raphson method"""
    approx = None
    guess = x / 2
    while approx != guess:
        approx = guess
        guess = (approx + x / approx) / 2
    return approx


if __name__ == '__main__':
    assertEqualsTolerance(math.sqrt(4), my_sqrt(2))
    # What other tests can you think of?
