# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        def build(left, right):
            if left > right:
                return

            val = postorder.pop()
            root = TreeNode(val)
            index = inorder.index(val)
            # 先遍历右子树，因为后续遍历pop的时候先拿到的是右子树的节点
            root.right = build(index + 1, right)
            root.left = build(left, index - 1)

            return root

        tree = build(0, len(inorder) - 1)
        return tree
