class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        s1 = s[::-1]
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        max_len = 0
        end = 0
        for i in range(0, n):
            for j in range(0, n):
                if s[i] == s1[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    index = n - j - 1
                    index = index + dp[i][j] - 1
                    if index == i:
                        max_len = dp[i][j]
                        end = i
        return s[end - max_len + 1:end + 1]


if __name__ == '__main__':
    res = Solution().longestPalindrome("a")
    print(res)
