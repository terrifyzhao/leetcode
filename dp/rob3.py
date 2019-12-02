# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        递归
        """
        if not root:
            return 0
        m = root.val
        if root.left:
            m += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            m += self.rob(root.right.left) + self.rob(root.right.right)
        return max(m, self.rob(root.left) + self.rob(root.right))

    def rob2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        每个节点返回两个值，第一个值表示不抢，第二个值表示抢
        """

        def myrob(root):
            if not root:
                return 0, 0

            l = myrob(root.left)
            r = myrob(root.right)

            a = max(l) + max(r)
            b = root.val + l[0] + r[0]

            return a, b

        return max(myrob(root))
