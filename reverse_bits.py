class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        m = 0
        for i in range(32):
            m = m << 1
            m = m | (n & 1)
            n = n >> 1
        return m

    def reverseBits2(self, n):
        res = list('{:032b}'.format(n))[::-1]
        return int(''.join(res), 2)


s = Solution()
r = s.reverseBits(2)
print(r)
