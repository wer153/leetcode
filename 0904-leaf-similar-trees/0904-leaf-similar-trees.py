# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return travalse(root1) == travalse(root2)

def travalse(root):
    stack = [root]
    leafs = []
    while stack:
        node = stack.pop()
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        if node.right is None and node.left is None:
            leafs.append(node.val)
    return leafs
