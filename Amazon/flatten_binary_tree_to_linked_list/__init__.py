# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def flatten(self, root):
        if root is None or root.right is None and root.left is None:
            return

        if root.left is not None:
            self.flatten(root.left)

            temp = root.right
            root.right = root.left
            root.left = None

            var = root.right

            while var.right is not None:
                var = var.right
            var.right = temp

        self.flatten(root.right)
