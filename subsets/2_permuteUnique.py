class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(nums, depth, res, path, used):
            if depth == len(nums):
                res.append(list(path))
                return

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])

                    dfs(nums, depth + 1, res, path, used)

                    used[i] = False
                    path.pop()

        res = []
        nums.sort()
        used = [False for _ in range(len(nums))]
        dfs(nums, 0, res, [], used)
        return res


print(Solution().permuteUnique([1, 1, 2]))
