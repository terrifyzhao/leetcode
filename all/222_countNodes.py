# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def tree_depth(self, root):
        depth = 0
        while root.left:
            root = root.left
            depth += 1
        return depth

    def exist(self, depth, index, node):
        left = 0
        right = pow(2, depth) - 1
        for _ in range(depth):
            mid = left + (right - left) // 2
            if index <= mid:
                node = node.left
                right = mid
            else:
                node = node.right
                left = mid + 1
        return node is not None

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        depth = self.tree_depth(root)
        if depth == 0:
            return 1

        left = 1
        right = pow(2, depth) - 1
        while left <= right:
            mid = left + (right - left) // 2

            # 如果节点存在，说明右侧还有更多节点，更新left
            if self.exist(depth, mid, root):
                left = mid + 1
            else:
                right = mid - 1
        print(left)
        return left + pow(2, depth) - 1


class Solution2(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0
        left = root
        h_l = 0
        while left:
            left = left.left
            h_l += 1
        right = root
        h_r = 0
        while right:
            right = right.right
            h_r += 1
        if h_l == h_r:
            return (1 << h_l) - 1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
Solution().countNodes(root)
