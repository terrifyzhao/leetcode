class Solution(object):
    def maxArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = nums[0]
        res = nums[0]

        for num in nums[1:]:
            max_num = max(max_num + num, num)
            res = max(max_num, res)

        return res


s = Solution()
result = s.maxArray([-5, 5, -3, -4, -1, 4])
print(result)
