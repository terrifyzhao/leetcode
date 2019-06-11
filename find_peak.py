class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + int((right - left) / 2)
            if nums[mid + 1] > nums[mid]:
                left = mid + 1
            else:
                right = mid
        return right


s = Solution()
r = s.findPeakElement([1, 2, 1, 3, 5, 6, 4])
print(r)
