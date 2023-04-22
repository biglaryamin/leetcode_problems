from math import ceil
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head):
    mapped = []
    n = 0
    while head:
        mapped.append(head)
        n += 1
        head = head.next
    k = n // 2 if n % 2 else ceil(n/2)
    return mapped[k]