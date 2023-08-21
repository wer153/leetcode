# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        batch, level = [root], 0
        while batch:
            next_batch = []
            level += 1
            for node in batch:
                if node and node.left:
                    next_batch += [node.left]
                if node and node.right:
                    next_batch += [node.right]
            batch = next_batch
        return level
