class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        max_data = []
        if len(nums) == 0:
            return max_data
        for i in range(len(nums) - k + 1):
            max_data.append(max(nums[i:i + k]))
        return max_data

    def maxSlidingWindow2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        win = []
        res = []
        for i, v in enumerate(nums):
            # i>=k是为了保证win里面有值，如果当前下标减去队首下标大于等于k说明窗口已经滑出去了，把队首元素移除
            if i >= k and i - win[0] >= k:
                win.pop(0)
            # win不为空，就循环一遍，确保新的值大于队列里的值，把队列里的值出队列
            while win and v >= nums[win[-1]]:
                win.pop()
            # 把下标存入win中
            win.append(i)
            # 如果下标大于k就把结果存入res
            if i >= k-1:
                res.append(nums[win[0]])
        return res


s = Solution()
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
res = s.maxSlidingWindow2(nums, k)
print(res)
