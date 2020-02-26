class Solution(object):
    def longestConsecutive2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            if nums[i - 1] + 1 == nums[i]:
                dp[i] = dp[i - 1] + 1
            if nums[i - 1] == nums[i]:
                dp[i] = dp[i - 1]
        return max(dp)

    def longestConsecutive(self, nums):
        if not nums:
            return 0

        s = set(nums)
        res = 0
        for i in s:
            if i - 1 not in s:
                cur = i
                cur_num = 1

                while cur + 1 in s:
                    cur += 1
                    cur_num += 1
                res = max(res, cur_num)
        return res
