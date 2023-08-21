# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from itertools import pairwise

def iterate_linked_list(node):
    while node:
        yield node
        node = node.next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        stack = [node for node in iterate_linked_list(head)]
        
        for node in stack:
            node.next = None
        
        tail = stack[-1]
        while stack:
            node =  stack.pop()
            if stack:
                node.next = stack[-1]
        return tail
