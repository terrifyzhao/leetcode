class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        char_list = [0] * 26
        for i in s:
            char_list[ord(i)-ord('a')] += 1
        for i in t:
            char_list[ord(i) - ord('a')] -= 1
            if char_list[ord(i) - ord('a')] < 0:
                return False
        return True


