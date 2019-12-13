# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def __init__(self):
        self.max_path = float("-inf")

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_gain(root)
        return self.max_path

    def max_gain(self, node):
        if not node:
            return 0
        left = max(self.max_gain(node.left), 0)
        right = max(self.max_gain(node.right), 0)

        new_path = node.val + left + right
        self.max_path = max(self.max_path, new_path)

        # 返回的是一条路径的值
        return node.val + max(left, right)
