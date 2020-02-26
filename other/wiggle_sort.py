class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        tmp = sorted(nums)
        mid = int((len(tmp) + 1) / 2)
        i = mid - 1
        j = len(tmp) - 1
        for k in range(len(tmp)):
            if k & 1 == 0:
                nums[k] = tmp[i]
                i -= 1
            else:
                nums[k] = tmp[j]
                j -= 1

    def wiggleSort2(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        mid = len(nums[::2])
        nums[::2], nums[1::2] = nums[:mid][::-1], nums[mid:][::-1]


s = Solution()
nums = [1, 2, 3, 4]
s.wiggleSort2(nums)
print(nums)
