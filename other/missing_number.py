class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            res += num
        for i in range(len(nums) + 1):
            res -= i
        return abs(res)


s = Solution()
r = s.missingNumber( [3,0,1])
print(r)
