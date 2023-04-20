class ListNode:
    def __init__(self) -> None:
        self.head = None


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Solution:
    def removeNthFromEnd(self, link_list, n):
        count = 1
        while True:
            if link_list.next is not None:
                if count == n-1:
                    link_list = link_list.next.next
                    count += 2
                else:
                    link_list = link_list.next
                    count += 1

            