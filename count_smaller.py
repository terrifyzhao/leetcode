class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        self.count = 0


class Solution(object):
    def countSmaller1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counts = []
        for index, num in enumerate(nums):
            count = 0
            for n in nums[index + 1:]:
                if n < num:
                    count += 1
            counts.append(count)
        return counts

    def countSmaller2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        root = None
        res = [0 for _ in nums]
        for i in reversed(range(len(nums))):
            root = self.insert(root, nums[i], res, i)
        return res

    def insert(self, root, val, res, res_index):
        if root is None:
            root = TreeNode(val)
        elif val <= root.val:
            root.count += 1
            root.left = self.insert(root.left, val, res, res_index)
        elif val > root.val:
            res[res_index] += root.count + 1
            root.right = self.insert(root.right, val, res, res_index)

        return root

    def countSmaller(self, nums):
        import bisect
        res = []
        l = []
        for num in nums[::-1]:
            idx = bisect.bisect_left(l, num)
            res.append(idx)
            bisect.insort(l, num)

        res.reverse()
        return res


s = Solution()
res = s.countSmaller([5, 2, 6, 1])
print(res)
