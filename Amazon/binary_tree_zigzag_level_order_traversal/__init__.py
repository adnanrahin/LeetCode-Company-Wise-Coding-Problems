import collections


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    dictionary = None

    def zigzagLevelOrder(self, root):
        self.dictionary = collections.defaultdict(list)
        self.level_order_traversal(0, root)
        return self.dictionary.values()

    def level_order_traversal(self, level, root):
        if root is None:
            return

        if level % 2 == 0:
            self.dictionary[level].append(root.val)
        else:
            self.dictionary[level].insert(0, root.val)

        self.level_order_traversal(level + 1, root.left)
        self.level_order_traversal(level + 1, root.right)
