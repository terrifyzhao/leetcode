class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        begin = 0
        end = len(s) - 1
        while begin < end:
            tmp = s[begin]
            s[begin] = s[end]
            s[end] = tmp
            begin += 1
            end -= 1


s = Solution()
a = ["h", "e", "l", "l", "o"]
s.reverseString(a)
print(a)
