import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        length = len(self.nums)
        random.randint(0, length)


# Your Solution object will be instantiated and called as such:
obj = Solution([1, 2, 3, 4])
param_1 = obj.reset()
param_2 = obj.shuffle()

