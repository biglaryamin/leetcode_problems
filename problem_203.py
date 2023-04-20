# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def removeElements(head, problem_val):

    while head.val != None:
        if head.next.val == problem_val:
            head = head.next.next
            continue

        head = head.next


def print_linkedlist_elements(head):
    while head.val != None:
        print(head.val, " ")
        head = head.next


Node1 = ListNode(1)
Node2 = ListNode(2)
Node3 = ListNode(3)
Node4 = ListNode(4)
Node5 = ListNode(5)
Node6 = ListNode(6)

Node1.next = Node2
Node1.next.next = Node3
Node1.next.next.next = Node4
Node1.next.next.next.next = Node5
Node1.next.next.next.next.next = Node6


removeElements(Node1, 3)
print_linkedlist_elements(Node1)