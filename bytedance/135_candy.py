class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0
        n = len(ratings)
        res = [1 for _ in range(n)]
        flag = True
        while flag:
            flag = False
            for i in range(0, n):
                if i < n - 1 and ratings[i] > ratings[i + 1] and res[i] <= res[i + 1]:
                    res[i] = res[i + 1] + 1
                    flag = True
                if i > 0 and ratings[i - 1] < ratings[i] and res[i - 1] >= res[i]:
                    res[i] = res[i - 1] + 1
                    flag = True

        return sum(res)


class Solution2(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0
        n = len(ratings)
        left = [1 for _ in range(n)]
        right = left[:]

        for i in range(1, n):
            if ratings[i - 1] < ratings[i]:
                left[i] = left[i - 1] + 1

        count = left[-1]
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1
            count += max(left[i], right[i])
        return count
