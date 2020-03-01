class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        if len(intervals) < 2:
            return intervals

        intervals.sort(key=lambda x: x[0])
        start, end = 0, 1
        interval = intervals[0]
        res = []

        for i in range(1, len(intervals)):
            if interval[end] >= intervals[i][start]:
                interval = [interval[start], max(intervals[i][end], interval[end])]
            else:
                res.append(interval)
                interval = intervals[i]
        res.append(interval)
        return res
