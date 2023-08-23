# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from operator import gt, lt, eq

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root:
            node, parent = find(root, key)
            if not node:
                pass
            elif node.left and node.right:
                node.val = pop_smallest_gt(node)
            else:
                child = node.left or node.right or None
                if node == root:
                    root = child
                else:
                    if parent.left == node:
                        parent.left = child
                    elif parent.right == node:
                        parent.right = child
        return root

def find(root, val, parent=None):
    if not root or root.val == val:
        return root, parent
    return find(
        root.right if root.val < val else root.left,
        val,
        root,
    )

def pop_smallest_gt(root):
    parent, node = root, root.right
    while node.left:
        parent, node = node, node.left
    if root == parent:
        parent.right = node.right
    else:
        parent.left = node.right or None
    return node.val
