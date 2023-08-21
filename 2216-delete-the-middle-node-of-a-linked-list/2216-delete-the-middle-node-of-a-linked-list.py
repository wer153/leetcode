class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_list = list(iterate_linked_list(head))
        size, target = len(node_list), len(node_list) // 2
        if target == 0:
            head = head.next
        else:
            for index, (prev, node) in enumerate(node_list):
                if index == target:
                    prev.next = node.next
                    break
        return head

def iterate_linked_list(head):
    prev, node = None, head
    while node:
        yield prev, node
        prev, node = node, node.next
