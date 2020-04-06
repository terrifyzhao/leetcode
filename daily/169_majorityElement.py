class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = nums[0]
        count = 1
        for n in nums[1:]:
            if count == 0:
                num = n
            if n == num:
                count += 1
            else:
                count -= 1
        return num
