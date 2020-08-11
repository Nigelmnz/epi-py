from typing import List, TypeVar, Union


T = TypeVar("T")


class Node:
    def __init__(self, value: T = None, next: "Node" = None):
        self.value = value
        self.next: Union[T, None] = next


class LinkedList:
    def __init__(self, init: List[T] = []):
        self.head = Node() if len(init) == 0 else Node(init[0])
        self.tail = self.head

        for x in init[1:]:
            self.tail.next = Node(x)
            self.tail = self.tail.next

    def __iter__(self):
        ptr = self.head
        while ptr:
            yield ptr.value
            ptr = ptr.next

    def __str__(self) -> str:
        return str(list(self.__iter__()))

    def __eq__(self, other: 'LinkedList'):
        a, b = self.head, other.head
        while a and b:
            if a.value != b.value:
                return False
            a, b = a.next, b.next
        return a is None and b is None
