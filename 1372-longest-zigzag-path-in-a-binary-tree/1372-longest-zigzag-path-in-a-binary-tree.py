# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

LEFT = 'left'
RIGHT = 'right'

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def travalse(node, last, count):
            nonlocal answer
            answer = max(answer, count)
            if node.left:
                travalse(node.left, last=LEFT, count=1 if last == LEFT else count + 1)
            if node.right:
                travalse(node.right, last=RIGHT, count=1 if last == RIGHT else count + 1)
        answer = 0
        if root: travalse(root, last=None, count=0)
        return answer
