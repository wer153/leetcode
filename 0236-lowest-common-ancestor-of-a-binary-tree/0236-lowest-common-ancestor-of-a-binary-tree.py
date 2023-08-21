# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find_paths(node, path):
            if node == p or node == q:
                paths.append(path)
            if node.left:
                find_paths(node.left, [*path, node.left])
            if node.right:
                find_paths(node.right, [*path, node.right])
        
        paths = []
        find_paths(root, [root])
        return [a for a, b in zip(*paths) if a==b][-1]
