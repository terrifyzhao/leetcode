class Solution(object):
    def longestPalindrome(self, s):
        r = s[::-1]
        max_len = 0
        max_end = 0

        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][0] = 1 if s[i] == r[0] else 0

        for i in range(len(s)):
            dp[0][i] = 1 if r[i] == s[0] else 0

        for i in range(len(s)):
            for j in range(len(r)):
                if s[i] == r[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    max_end = i

        return s[max_end - max_len + 1:max_end + 1]


a = Solution().longestPalindrome("babad")
print(a)
