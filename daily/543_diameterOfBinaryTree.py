# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    max_dia = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.dfs(root)
        return self.max_dia-1

    def dfs(self, root):
        if not root:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        self.max_dia = max(self.max_dia, left + right + 1)

        return max(left, right) + 1
