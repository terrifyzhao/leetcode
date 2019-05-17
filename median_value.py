class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        for i in range(len(self.nums)):
            if num > self.nums[i]:
                for i in range(i, len(self.nums)):
                    pass



    def findMedian(self):
        """
        :rtype: float
        """
