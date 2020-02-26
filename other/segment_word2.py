# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
# add spaces in s to construct a sentence where each word is a valid dictionary word.
# Return all such possible sentences.
#
# Note:
#
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.

class Solution(object):
    def wordbreak(self, s, wordDict):
        if len(s) == 0 or not wordDict:
            return []
        res = [0] * (len(s) + 1)
        res[0] = 1
        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if res[j] == 1 and s[j:i] in wordDict:
                    res[i] = 1
        if res[-1] == 0:
            return []
        result = []
        self.dfs(s, wordDict, 0, [], result, '')
        return result

    def dfs(self, s, wordDict, begin, tmp, result, word):
        tmp.append(word)
        begin += len(word)
        if begin == len(s):
            result.append(' '.join(tmp[1:]))
        for w in wordDict:
            if len(w) + begin <= len(s) and s[begin:begin + len(w)] == w:
                self.dfs(s, wordDict, begin, tmp, result, w)
        tmp.pop()
        begin -= len(word)


if __name__ == '__main__':
    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    # s = "catsanddog"
    # wd = ["cat", "cats", "and", "sand", "dog"]
    so = Solution()
    res = so.wordbreak(s, wordDict)
    print(res)
