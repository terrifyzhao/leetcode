class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 3:
            return []
        res = []

        nums.sort()
        n = len(nums)
        for i in range(n - 1):

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            first = nums[i]
            start = i + 1
            end = n - 1

            while start < end:
                num_sum = nums[start] + nums[end]
                if -first == num_sum:
                    res.append([first, nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1

                elif -first < num_sum:
                    end -= 1
                else:
                    start += 1
        return res
