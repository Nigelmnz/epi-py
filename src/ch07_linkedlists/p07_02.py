"""
Problem: Reverse a linked list between the ath and bth node.

"""

from src.library.linkedlist import LinkedList, Node


def reverse_list(input: LinkedList, a: int, b: int) -> LinkedList:
    # First, find A and the node before it
    a_pred, a_node = Node(next=input.head), input.head
    for _ in range(0, a):
        a_pred = a_node
        a_node = a_node.next

    # Now reverse the list between a and b
    for _ in range(a, b):
        temp = a_node.next
        a_node.next, temp.next, a_pred.next = temp.next, a_pred.next, temp

    # Specific to this linked list implementation,
    # update our head if it changed.
    if a == 0:
        input.head = a_pred.next
    return input
