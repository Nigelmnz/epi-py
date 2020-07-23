"""
Problem: Given a list of unique elements and a integer N, return a uniformly
random subset of size N.

Solution:
Swap in a random element for the first k elements of the list. Return the first
k elements. As every element has an equal probability of being selected for the
kth slot, the result is a uniformly random subset.

"""

from typing import List
import random


def solution(input: List[float], size: int):
    """
        Note that this will mutate your input!
    """
    for i in range(size):
        r = random.randint(i, size - 1)
        input[i], input[r] = input[r], input[i]
    return input[:size]
