class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = ord(list(s)[0]) - ord('A') + 1
        for i in list(s[1:]):
            num = (ord(i) - ord('A') + 1) + 26 * num
        return num


s = Solution()
res = s.titleToNumber('ZY')
print(res)
