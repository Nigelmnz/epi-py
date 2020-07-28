from typing import List
import pytest
from src.ch05_arrays.p05_11 import solution


@pytest.mark.parametrize("args, result", [
    ([2, 0, 1], [2, 1, 0]),
    ([1, 0, 3, 2], [1, 2, 0, 3]),
    ([3, 2, 1, 0], []),
    ([7, 8, 4, 1, 3, 5, 6, 0, 2], [7, 8, 4, 1, 3, 5, 6, 2, 0]),
    ([234, 12, 156], [234, 156, 12])
])
def test_solution(args: List[float], result: float):
    assert solution(args) == result
