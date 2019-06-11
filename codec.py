class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from queue import Queue


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = ''
        queue = []
        queue.append(root)
        while queue:
            root = queue.pop(0)
            if root:
                res += str(root.val)
                queue.append(root.left)
                queue.append(root.right)
            else:
                res += 'None'
            res += ','
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        tree = data.split(',')
        if tree[0] == 'None':
            return None
        queue = []
        root = TreeNode(tree[0])
        queue.append(root)
        i = 1
        while queue:
            cur = queue.pop(0)
            if not cur:
                continue
            cur.left = TreeNode(tree[i]) if tree[i] != 'None' else None
            cur.right = TreeNode(tree[i + 1]) if tree[i + 1] != 'None' else None
            i += 2
            queue.append(cur.left)
            queue.append(cur.right)
        return root


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    codec = Codec()
    res = codec.deserialize(codec.serialize(root))
    print(res)
