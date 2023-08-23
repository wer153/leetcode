# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque, defaultdict

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        depth_to_sum = defaultdict(int)
        queue = deque()
        if root:
            queue.append((root, 1))
        while queue:
            node, depth = queue.popleft()
            depth_to_sum[depth] += node.val
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
        max_level_sum = max(depth_to_sum.values())
        for depth, level_sum in depth_to_sum.items():
            if level_sum == max_level_sum:
                return depth
