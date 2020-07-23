from typing import Tuple, List
import pytest
from src.ch05_arrays.p05_12 import solution


@pytest.mark.parametrize("args", [
    ([1, 2, 3, 4, 5, 6, 7, 8], 4),
    ([1, 2, 3, 4, 5, 6, 7, 8], 2),
    ([1, 2, 3, 4, 5, 6, 7, 8], 3),
    ([1, 2, 3, 4, 5, 6, 7, 8], 1),
])
def test_solution(args: Tuple[List[float], int]):
    data, size = args
    result = solution(data, size)
    assert len(result) == size
    assert len(set(result)) == len(result)
