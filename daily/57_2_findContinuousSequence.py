from collections import deque


class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        start = 1
        tmp = deque()
        tmp_sum = 0
        for i in range(1, target):
            tmp.append(i)
            tmp_sum += i

            while tmp_sum > target:
                tmp_sum -= start
                tmp.popleft()
                start += 1

            if tmp_sum == target:
                res.append(list(tmp))
        return res
