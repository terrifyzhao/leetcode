class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0 for _ in range(len(s))]
        max_len = 0
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    if i >= 2:
                        dp[i] = dp[i - 2] + 2
                    else:
                        dp[i] = 2
                elif s[i - 1] == ')' and i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    if i - dp[i - 1] >= 2:
                        pre = i - dp[i - 1] - 2
                    else:
                        pre = 0
                    dp[i] = dp[i - 1] + dp[pre] + 2
                max_len = max(max_len, dp[i])
        return max_len
