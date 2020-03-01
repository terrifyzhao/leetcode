class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        nums = [envelope[1] for envelope in envelopes]

        dp = [0 for _ in range(len(nums))]
        dp[0] = 1

        max_len = 1
        for i in range(1, len(nums)):
            max_j = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    max_j = max(max_j, dp[j])
            dp[i] = max_j + 1
            max_len = max(dp[i], max_len)
        return max_len
