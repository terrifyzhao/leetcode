import random


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.origin = nums.copy()
        self.output = nums.copy()

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.origin

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(len(self.output)):
            j = random.randint(0, len(self.output) - 1)
            self.output[i], self.output[j] = self.output[j], self.output[i]
        return self.output


# Your Solution object will be instantiated and called as such:
obj = Solution([1, 2, 3, 4])
param_1 = obj.reset()
param_2 = obj.shuffle()

print(param_2)
print(param_1)
