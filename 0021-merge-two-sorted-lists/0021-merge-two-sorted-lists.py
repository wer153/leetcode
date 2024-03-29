from itertools import pairwise
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2
        for prev, curr in pairwise(iterate_linked_lists(list1, list2)):
            prev.next = curr
        return list1 if list1.val <= list2.val else list2
        

def iterate_linked_lists(head1, head2):
    while head1 and head2:
        if head1.val <= head2.val:
            yield head1
            head1 = head1.next
        else:
            yield head2
            head2 = head2.next
    else:
        head = head1 or head2
        while head:
            yield head
            head = head.next
