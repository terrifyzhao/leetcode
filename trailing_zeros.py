class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n >= 5:
            n = n // 5
            res += n
        return res


if __name__ == '__main__':
    s = Solution()
    r = s.trailingZeroes(1000)
    print(r)
