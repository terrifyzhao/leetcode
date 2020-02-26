# one number
# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# 相同的数字异或为0，0和某数字异或结果为某数字


class Solution(object):
    def singleNumber(self, nums):
        num = nums[0]
        for i in nums[1:]:
            num = num ^ i
        return num


s = Solution()
number = s.singleNumber([1, 2, 2, 1, 3])
print(number)
