import sys


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.nums.append(x)

    def pop(self):
        """
        :rtype: None
        """
        self.nums.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.nums[len(self.nums) - 1]

    def getMin(self):
        """
        :rtype: int
        """
        min_num = self.nums[0]
        for num in self.nums[1:]:
            if num < min_num:
                min_num = num
        return min_num


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(1)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3)
print(param_4)
