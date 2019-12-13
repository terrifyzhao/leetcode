class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums = sorted(nums)

        count = 1
        max_count = count
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    count += 1
                else:
                    max_count = max(max_count, count)
                    count = 1
        return max(max_count, count)

    def longestConsecutive2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        num_set = set()
        for num in nums:
            num_set.add(num)
        max_count = 1
        for num in nums:
            # 因为有这个判断，所有只有最小的值会进入循环，所以时间复杂度是O(N)
            if not num_set.__contains__(num - 1):
                count = 1

                while num_set.__contains__(num + 1):
                    num += 1
                    count += 1
                max_count = max(max_count, count)

        return max_count


if __name__ == '__main__':
    print(Solution().longestConsecutive2([1, 2, 0, 1]))
