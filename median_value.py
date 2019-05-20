import heapq


# 先把第一个值放在小根堆里
# 下一个值是偶数位置，先判断是否比小根堆的根值大，大的话就放到小根堆，然后pop出根值，放入到大根堆
# 下一个值是奇数位置，先判断是否比大根堆的根值小，小的话就放大大根堆，然后pop出根值，放入到小根堆
# 返回值看哪个堆多久返回哪个堆的根值，一样就取根值的均值
# python没有大根堆，只有小根堆，取反来代替大根堆

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []
        self.big = []
        self.length = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if self.length & 1 == 0:
            if self.length > 1 and num < -self.big[0]:
                num = -heapq.heappushpop(self.big, -num)
            heapq.heappush(self.small, num)
        else:
            if self.length > 0 and num > self.small[0]:
                num = heapq.heappushpop(self.small, num)
            heapq.heappush(self.big, -num)
        self.length += 1

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) == len(self.big):
            return (self.small[0] - self.big[0]) / 2
        elif len(self.small) > len(self.big):
            return self.small[0]
        else:
            return -self.big[0]


if __name__ == '__main__':
    obj = MedianFinder()
    obj.addNum(-1)
    obj.addNum(-2)
    obj.addNum(-2)
    obj.addNum(-3)
    # obj.addNum(1)
    # obj.addNum(6)
    # obj.addNum(7)

    # obj.addNum(-1)
    # print(obj.findMedian())
    # obj.addNum(-2)
    # print(obj.findMedian())
    # obj.addNum(-3)
    # print(obj.findMedian())
    # obj.addNum(-4)
    # print(obj.findMedian())
    # obj.addNum(-5)
    # print(obj.findMedian())
    # obj.addNum(2)
    # obj.addNum(5)
    # obj.addNum(6)
    # print(obj.small)
    # print(obj.small)
    # print(obj.big)
    param_2 = obj.findMedian()
    # param_2 = obj.findMedian()
    print(param_2)
