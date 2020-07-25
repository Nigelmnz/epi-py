"""
Problem: Given a string represention of a number in base A, and an int for base
A and B, convert the given number from base A to B

Solution: Convert to Base 10, then to Base B.

"""


def solution(num: str, base_from: int, base_to: int):
    hexdigits = "0123456789ABCDEF"

    # First, convert the number to base 10. By continuously multiplying the
    # found total by the base as we add digits of decreasing power,
    # the previously added digits will be mutliplied by the correct base^power.

    # As an example, for the number with digits "XYZ", multipying the total by
    # the base each time a digit is added results in the expression:
    # Xb^2 + Yb + Z, which will equal the total number.
    num_value = 0
    for c in num:
        num_value = num_value * base_from + hexdigits.index(c)

    # Now convert it to our target base. N % base will find the lowest order
    # digit of N. Dividing by base will let us explore higher order digits.
    result = ""
    while num_value > 0:
        result = str(hexdigits[num_value % base_to]) + result
        num_value //= base_to

    return result
