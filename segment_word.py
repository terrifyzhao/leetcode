# segment word

# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.
#
# Note:
#
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if len(s) == 0 or not wordDict:
            return False
        max_stride = max([len(word) for word in wordDict])
        result = [0] * (len(s) + 1)
        result[0] = 1
        # 终止位置
        for i in range(1, len(s) + 1):
            # 起始位置
            for j in range(i - max_stride, i):
                if j < 0:
                    continue
                # 想象为爬楼梯，result[j]为1表示能到达的楼层，这里表示匹配上的字符串，
                # 还需要保证字符串在dict里面，如果两者都满足，则跟新result内容
                if result[j] == 1 and s[j:i] in wordDict:
                    result[i] = 1
        if result[-1] == 1:
            return True
        else:
            return False


s = Solution()
word_break = s.wordBreak("cars", ["car", "ca", "rs"])
print(word_break)


def wordBreak(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(len(s) + 1):
        if not dp[i]:
            continue
        for word in wordDict:
            if i + len(word) <= len(s) and s[i:i + len(word)] == word:
                dp[i + len(word)] = True
    return dp[len(s)]
