class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        a1 = nums[0]
        a2 = max(nums[0], nums[1])
        a3 = max(a1+nums[2], a2)

        """
        a = 0
        b = 0
        for num in nums:
            b, a = max(a + num, b), b
        return a
