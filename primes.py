# https://www.cnblogs.com/grandyang/p/4462810.html

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        else:
            res = [1] * n
            res[0], res[1] = 0, 0
            for i in range(2, int(n ** 0.5) + 1):
                if res[i] == 1:
                    res[i * i:n:i] = [0] * len(res[i * i:n:i])
        return sum(res)


s = Solution()
r = s.countPrimes(10)
print(r)
