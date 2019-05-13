class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(k - 1):
            max_num = max(nums)
            nums.remove(max_num)
        return max(nums)


s = Solution()
res = s.findKthLargest([3,2,3,1,2,4,5,5,6], 4)
print(res)
