import pytest
from src.ch07_linkedlists.p07_02 import reverse_list
from src.library.linkedlist import LinkedList


@pytest.mark.parametrize("args, result", [
    ((LinkedList([1, 2, 3, 4, 5, 6]), 0, 5), LinkedList([6, 5, 4, 3, 2, 1])),
    ((LinkedList([1, 2, 3, 4, 5, 6]), 2, 4), LinkedList([1, 2, 5, 4, 3, 6])),
    ((LinkedList([1, 2, 3]), 0, 2), LinkedList([3, 2, 1])),
    ((LinkedList([1, 2, 3]), 0, 1), LinkedList([2, 1, 3])),
    ((LinkedList([1]), 0, 0), LinkedList([1])),
    ((LinkedList([]), 0, 0), LinkedList([])),
])
def test_solution(args, result):
    assert reverse_list(*args) == result
