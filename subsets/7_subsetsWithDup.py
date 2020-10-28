class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(cur, begin):
            res.append(list(cur))

            for i in range(begin, len(nums)):
                if i > begin and nums[i] == nums[i - 1]:
                    continue
                cur.append(nums[i])
                dfs(cur, i + 1)
                cur.pop()

        res = []
        nums.sort()
        dfs([], 0)
        return res


print(Solution().subsetsWithDup([1, 2, 1]))
