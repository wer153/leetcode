# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def travalse(node, max_val):
            if node.val == max_val:
                nonlocal answer
                answer +=1
            if node.left:
                travalse(node.left, max_val=max(max_val, node.left.val))
            if node.right:
                travalse(node.right, max_val=max(max_val, node.right.val))

        answer = 0
        travalse(root, root.val)
        return answer
