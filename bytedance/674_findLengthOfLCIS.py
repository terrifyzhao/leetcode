class Solution(object):
    def findLengthOfLCIS2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_len = 1
        start = 0

        n = len(nums)

        for i in range(n):
            if i > 0:
                if nums[i] > nums[i - 1]:
                    max_len = max(max_len, i - start + 1)
                else:
                    start = i
        return max_len

    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1] * len(nums)

        for i in range(1, len(nums)):

            if nums[i - 1] < nums[i]:
                dp[i] = dp[i - 1] + 1

        return max(dp)


print(Solution().findLengthOfLCIS([1, 3, 5, 4, 2, 3, 4, 5]))
