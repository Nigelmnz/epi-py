from typing import Tuple
import pytest
from src.ch04_ptypes.p04_07 import power, power_recur, power_brute


@pytest.mark.parametrize("args", [
    (2, 3),
    (0, 5),
    (5, 0),
    (1, 4),
    (4, 1),
    (20000, 4),
    (5, 3000),
    (2.0234, 3),
    (2342, 1233)
])
def test_power(args: Tuple[float, int]):
    assert power_brute(*args) == args[0]**args[1]
    assert power_recur(*args) == args[0]**args[1]
    assert power(*args) == args[0]**args[1]
