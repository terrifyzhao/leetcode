# Find the length of the longest substring T of a given string
# (consists of lowercase letters only) such that every character in
# T appears no less than k times.


class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) == 0 or len(s) < k:
            return 0
        if k < 2:
            return len(s)
        return self.count(s, k, 0, len(s) - 1)

    def count(self, s, k, p1, p2):
        if p2 - p1 + 1 < k:
            return 0
        dic = {}
        for i in range(p1, p2 + 1):
            dic[s[i]] = dic.get(s[i], 0) + 1
        while p2 - p1 + 1 >= k > dic[s[p1]]:
            p1 += 1
        while p2 - p1 + 1 >= k > dic[s[p2]]:
            p2 -= 1
        if p2 - p1 + 1 < k:
            return 0
        for i in range(p1, p2 + 1):
            if dic[s[i]] < k:
                return max(self.count(s, k, p1, i - 1), self.count(s, k, i + 1, p2))
        return p2 - p1 + 1
