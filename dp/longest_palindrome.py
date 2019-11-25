import numpy as np


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        p = np.zeros(shape=(length, length))
        max_len = 0
        max_str = ''
        for l in range(1, length + 1):
            for start in range(0, length):
                end = start + l - 1
                if end >= length:
                    break
                p[start][end] = (l == 1 or l == 2 or p[start + 1][end - 1]) and s[start] == s[end]
                if p[start][end] and l > max_len:
                    max_len = l
                    max_str = s[start:end + 1]
        return max_str

    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str


        状态转移方程
        p[i][j] = p[i+1][j-1] and s[i]==s[j]

        空间优化：
        实际只需要内存循环的值保留就行了
        p[j] = p[j-1] and s[i]==s[j]


        """
        length = len(s)
        p = [False for _ in range(length)]
        max_str = ''
        # 从尾部开始遍历
        for i in range(length - 1, -1, -1):
            for j in range(length - 1, -1, -1):
                # j-i<3用来做初始化操作，即只有1个字符或者2个字符的时候置为True
                p[j] = s[i] == s[j] and (j - i < 3 or p[j - 1])
                if p[j] and j - i + 1 > len(max_str):
                    max_str = s[i:j + 1]

        return max_str
