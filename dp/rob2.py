class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def rob_in(num):
            a, b = 0, 0
            for n in num:
                b, a = max(a + n, b), b
            return b

        return max(rob_in(nums[:-1]), rob_in(nums[1:])) if len(nums) != 1 else nums[0]


if __name__ == '__main__':
    s = Solution().rob([1])
    print(s)
