from typing import Tuple
import pytest
from src.ch06_strings.p06_02 import solution


@pytest.mark.parametrize("args, answer", [
    (("615", 7, 13), "1A7"),
    (("1232", 4, 13), "86"),
    (("AB36", 12, 15), "5906"),
    (("AB36FFF", 16, 2), "1010101100110110111111111111"),
])
def test_solution(args: Tuple[str, int, int], answer: str):
    assert solution(*args) == answer
