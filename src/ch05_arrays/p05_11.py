"""
Problem: Given a permutation, return the next one in lexicographic order
"""

from typing import List


def solution(input: List[float]):
    if list(reversed(input)) == list(range(len(input))):
        return []

    # From the right, find the first digit that's less than its predecessor.
    # This is the digit we should increment by swapping.
    target_i = next(i for i in range(len(input)-2, -1, -1)
                    if input[i] < input[i+1])

    # Of every digit to the right of target, which would be the
    # smallest increase to swap in?
    swap_i = next(i for i in reversed(range(target_i+1, len(input)))
                  if input[target_i] < input[i])

    # Swap em
    input[target_i], input[swap_i] = input[swap_i], input[target_i]

    # Reverse everything after the target, giving us the lowest order sequence
    # after our new digit
    input[target_i + 1:] = reversed(input[target_i+1:])

    return input
