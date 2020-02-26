# majority element

# Given an array of size n, find the majority element. The majority element is the element that
# appears more than ⌊ n/2 ⌋ times.

# 遍历数组，计数器为0则赋值当前值，如果和赋值相同，则计数器+1反之-1，最后返回赋值，前提必须出现次数大于n/2

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, count = 0, 0

        for i in nums:
            if count == 0:
                res = i
                count += 1
            elif res == i:
                count += 1
            else:
                count -= 1
        return res


s = Solution()
number = s.majorityElement([1, 2, 2, 2, 3])
print(number)
