from collections import deque
import math


class Solution(object):
    def getPermutation2(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 0:
            return ''
        res = []
        queue = deque()
        queue.append([])

        for num in range(n):
            for _ in range(len(queue)):
                tmp = queue.popleft()
                for j in range(len(tmp) + 1):
                    per = list(tmp)
                    per.insert(j, str(num + 1))
                    if len(per) == n:
                        res.append(per)
                    else:
                        queue.append(per)
        for i, r in enumerate(res):
            res[i] = int(''.join(r))
        res.sort()
        return res[k - 1]

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [str(i) for i in range(1, n + 1)]
        res = ''
        k = k - 1

        while n > 0:
            n -= 1
            a, k = divmod(k, math.factorial(n))
            res += nums.pop(a)
        return res

Solution().getPermutation(3,5)