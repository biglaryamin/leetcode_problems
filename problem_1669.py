# Definition for singly-linked list.
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        temp = node.data
        while node.next != None:
            if node.data == a:
                temp = node.next
                node.next = list2

            node = node.next






# Your Solution object will be instantiated and called as such:
# obj = Solution()
