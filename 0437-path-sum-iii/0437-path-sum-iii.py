# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from itertools import accumulate

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        answer = 0
        def travalse(node, visited=[]):
            nonlocal answer
            answer += len([
                True for local_sum in accumulate(visited)
                if targetSum == local_sum
            ])
            if node.left:
                travalse(node.left, [node.left.val, *visited])
            if node.right:
                travalse(node.right, [node.right.val, *visited])
        if root:
            travalse(root, [root.val])
        return answer
