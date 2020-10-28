class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(depth, path):
            if depth == len(nums):
                res.append(list(path))
                return

            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])

                    dfs(depth + 1, path)

                    used[i] = False
                    path.pop()

        res = []
        used = [False for _ in range(len(nums))]
        dfs(0, [])
        return res


print(Solution().permute([1, 2, 3]))
