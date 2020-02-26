class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = [0] * 26
        for i in s:
            l[ord(i) - ord('a')] += 1

        for n in range(len(s)):
            if l[ord(s[n]) - ord('a')] == 1:
                return n
        return -1
