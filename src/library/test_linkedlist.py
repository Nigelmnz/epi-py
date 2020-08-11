# from typing import List
# import pytest
from src.library.linkedlist import LinkedList


def test_init():
    assert list(LinkedList([1, 2, 3])) == [1, 2, 3]


def test_eq():
    assert LinkedList([1, 2, 3]) == LinkedList([1, 2, 3])
