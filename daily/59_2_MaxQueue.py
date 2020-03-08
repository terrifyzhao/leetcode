from collections import deque


class MaxQueue(object):

    def __init__(self):
        self.queue = deque()
        self.ori_queue = deque()

    def max_value(self):
        """
        :rtype: int
        """
        return self.queue[0] if self.queue else -1

    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)
        self.ori_queue.append(value)

    def pop_front(self):
        """
        :rtype: int
        """
        if not self.queue:
            return -1
        res = self.ori_queue.popleft()
        if res == self.queue[0]:
            self.queue.popleft()
        return res


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
