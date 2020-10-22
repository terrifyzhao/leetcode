# 最长公共子序列
def longestCommonSubsequence(text1, text2):
    l1 = len(text1) + 1
    l2 = len(text2) + 1
    dp = [[0 for _ in range(l2)] for _ in range(l1)]

    for i in range(1, l1):
        for j in range(1, l2):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    return dp[-1][-1]

# 最长公共子串