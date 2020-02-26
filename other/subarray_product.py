class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num, min_num, res = nums[0], nums[0], nums[0]

        for num in nums[1:]:
            tmp_max = max_num
            tmp_min = min_num
            max_num = max(num, tmp_max * num, tmp_min * num)
            min_num = min(num, tmp_max * num, tmp_min * num)
            if max(max_num, min_num) > res:
                res = max(max_num, min_num)
        return res


s = Solution()
result = s.maxProduct([-4, -3, -2])
print(result)
