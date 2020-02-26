# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        tree = []
        if not root:
            return tree

        tree.append(root.val)

        left = self.preorderTraversal(root.left)
        for i in left:
            tree.append(i)

        right = self.preorderTraversal(root.right)
        for i in right:
            tree.append(i)

        return tree


class Solution2(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []

        self.order(res, root, 0)

        return res

    def order(self, res, root, level):
        if not root:
            return
        if len(res) == level:
            res.append([])
        res[level].append(root.val)
        self.order(res, root.left, level + 1)
        self.order(res, root.right, level + 1)


class Solution3(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.res = 0
        self.traverse(root)
        return self.res

    def traverse(self, root):
        # 先遍历到左子树的最左边，因为是搜索树，所以最左边是最小值
        if root.left:
            self.traverse(root.left)

        self.k -= 1

        if self.k == 0:
            self.res = root.val
            return

        if root.right:
            self.traverse(root.right)
