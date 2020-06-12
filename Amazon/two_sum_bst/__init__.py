# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    s = set()

    def findTarget(self, root, k):
        self.s = set()

        return self.find_target(root, k)

    def find_target(self, root, target):
        if root is None:
            return False
        if target - root.val in self.s:
            return True
        self.s.add(root.val)
        return self.find_target(root.left, target) or self.find_target(root.right, target)
