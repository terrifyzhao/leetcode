class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        for c in s.split(' '):
            if c:
                res.append(c)
        return ' '.join(res[::-1])
