class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.quick(nums, 0, len(nums) - 1, k)

    def quick(self, nums, start, end, k):
        if start > end:
            return nums[0]
        pivot_index = self.partition(nums, start, end)
        if pivot_index == k - 1:
            return nums[pivot_index]
        elif pivot_index < k - 1:
            return self.quick(nums, pivot_index + 1, end, k)
        else:
            return self.quick(nums, start, pivot_index - 1, k)

    def partition(self, nums, start, end):

        pivot = nums[start]
        left = start
        right = end
        while left != right:
            while left < right and nums[right] < pivot:
                right -= 1
            while left < right and nums[left] >= pivot:
                left += 1
            if left < right:
                tmp = nums[left]
                nums[left] = nums[right]
                nums[right] = tmp

        nums[start] = nums[left]
        nums[left] = pivot

        return left


s = Solution()
res = s.findKthLargest([3, 2, 5, 6], 4)
print(res)
