class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(cur, begin):
            res.append(list(cur))

            for i in range(begin, len(nums)):
                cur.append(nums[i])
                dfs(cur, i + 1)
                cur.pop()

        res = []
        dfs([], 0)
        return res


print(Solution().subsets([1, 2, 3]))
