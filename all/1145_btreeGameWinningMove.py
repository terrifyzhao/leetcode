# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def btreeGameWinningMove(self, root, n, x):
        """
        :type root: TreeNode
        :type n: int
        :type x: int
        :rtype: bool
        """

        self.left_count = 0
        self.right_count = 0

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            if root.val == x:
                self.left_count = left
                self.right_count = right
            return left + right

        dfs(root)
        parent = n - self.left_count - self.right_count - 1
        for i in [self.left_count, self.right_count, parent]:
            if i > n // 2:
                return True
        return False


if __name__ == '__main__':
    Solution().btreeGameWinningMove()
