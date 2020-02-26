# class Solution(object):
#     def rotate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         for index, num in enumerate(nums[n - k:] + nums[0:n - k]):
#             nums[index] = num
#         return nums
#
#
# class Solution(object):
#     def rotate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         for i in range(k):
#             tmp = nums.pop()
#             nums.insert(0, tmp)
#
#         return nums


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        self.tmp = 0
        self.reverse(nums, 0, n - k - 1)
        self.reverse(nums, n - k, n - 1)
        self.reverse(nums, 0, n - 1)

    def reverse(self, nums, begin, end):
        while begin < end:
            self.tmp = nums[begin]
            nums[begin] = nums[end]
            nums[end] = self.tmp
            begin += 1
            end -= 1


s = Solution()
result = s.rotate([1, 2, 3, 4, 5, 6, 7], 10)
print(result)
