class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 for _ in range(len(nums))]
        dp[0] = 1

        max_len = 0
        for i in range(1, len(nums)):
            max_len_j = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    max_len_j = max(max_len_j, dp[j])
            dp[i] = max_len_j + 1
            max_len = max(max_len, dp[i])
        return max_len


Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
