import sys

max_num = sys.maxsize


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a = max_num
        b = max_num
        for num in nums:
            if num <= a:
                a = num
            elif num <= b:
                b = num
            else:
                return True
        return False


s = Solution()
res = s.increasingTriplet([1, 1, 1, 1])
print(res)
