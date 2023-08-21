# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        vals = [node.val for node in iterate_linked_list(head)]
        return max(a + b for a, b in zip(vals[:len(vals)],vals[len(vals)::-1]))

def iterate_linked_list(head):
    while head:
        yield head
        head = head.next
