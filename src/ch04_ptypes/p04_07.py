"""
Problem: Given a float X, and a positive integer Y, compute X^Y.

"""


def power_brute(x: float, y: int) -> float:
    """
        Solution A: Just mutiply X, Y times. Runs in O(n),
        where n is the size of y.
    """
    result = 1
    for n in range(y):
        result *= x
    return result


def power_recur(x: float, y: int) -> float:
    """
        Solution B: Consider that if y is even, then y = 2z, x^y = x^z * x^z.
        If it's not even, then y = 2z * x, x^y = x^z * x^z * x.
        Using this, we can recursively split the problem, vastly reducing
        the needed number of operations.
        Runs in O(log n).
    """
    if y == 0:
        return 1
    elif x == 0:
        return 0
    else:
        subresult = power_recur(x, y >> 1)
        return subresult * subresult * (x if y % 2 == 1 else 1)


def power(x: float, y: int) -> float:
    """
        Solution C: Same idea as before, but implemented iteratively.
        Runs in O(log n)
    """
    result = 1
    while y > 0:
        if y % 2 == 1:
            result *= x
        x *= x
        y >>= 1
    return result
