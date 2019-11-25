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
        length = []
        for i in range(1, len(s)):
            t = s[:i]
            