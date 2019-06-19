class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            if n & 1 == 1:
                count += 1
            n = n >> 1
        return count


s = Solution()
r = s.hammingWeight(1)
print(r)
