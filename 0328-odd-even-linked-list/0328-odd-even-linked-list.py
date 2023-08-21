# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        curr, even_head = head, head.next
        while curr.next and curr.next.next:
            even = curr.next
            curr.next = even.next
            even.next = curr.next.next    
            curr = curr.next
        curr.next = even_head
        return head

