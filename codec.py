class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from queue import Queue


class Codec:

    def sHelper(self, root, tree):
        if not root:
            tree.append(None)
            return
        tree.append(root.val)
        self.sHelper(root.left, tree)
        self.sHelper(root.right, tree)

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return None
        return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)

    def dHelper(self, data):
        if len(data) == 0:
            return None
        element = data.pop(0)
        if element is None:
            return None

        root = TreeNode(element)
        root.left = self.dHelper(data)
        root.right = self.dHelper(data)
        return root

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        l = data.split(',')
        return self.dHelper(l)


if __name__ == '__main__':
    codec = Codec()
    res = codec.serialize(codec.deserialize('[1, 2, 3, None, None, 4, 5]'))
    print(res)
