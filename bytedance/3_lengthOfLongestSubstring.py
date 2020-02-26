class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if len(s)==1:
            return 1
        dic = {}
        max_len = 0
        start = 0
        for index, i in enumerate(s):
            dic[i] = dic.get(i, 0) + 1
            while dic[i] > 1:
                s_s = s[start]
                dic[s_s] -= 1
                if dic[s_s] == 0:
                    del dic[s_s]
                start += 1
            max_len = max(max_len, index - start + 1)
        return max_len
