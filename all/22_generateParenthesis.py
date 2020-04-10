class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0:
            return ''
        res = []

        def dfs(s, left, right, res):
            if left == 0 and right == 0:
                res.append(s)

            if right < left:
                return

            if left > 0:
                dfs(s + '(', left - 1, right, res)
            if right > 0:
                dfs(s + ')', left, right - 1, res)

        dfs('', n, n, res)
        return res


class Solution2(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]

        # 当前括号数="(" + dp[可能的括号对数] + ")" + dp[剩下的括号对数]
        dp[i] = "(" + dp[j] + ")" + dp[i- j - 1]
        """
        if n <= 0:
            return ''

        dp = [None for _ in range(n + 1)]
        dp[0] = ['']

        for i in range(1, n + 1):
            cur = []
            for j in range(i):
                left = dp[j]
                right = dp[i - j - 1]
                for l in left:
                    for r in right:
                        cur.append('(' + l + ')' + r)
            dp[i] = cur

        return dp[-1]


def generateParenthesis(n):
    res = []

    def dfs(s, left, right):
        if left == n and right == n:
            res.append(s)
            return
        if left < right:
            return

        if left < n:
            dfs(s + '(', left + 1, right)

        if right < n:
            dfs(s + ')', left, right + 1)

    dfs('', 0, 0)
    return res


def generateParenthesis_dp(n):

    dp = [None for _ in range(n + 1)]
    dp[0] = ['']
    for i in range(1, n + 1):
        cur = []
        for j in range(i):
            left = dp[j]
            right = dp[i - 1 - j]
            for l in left:
                for r in right:
                    cur.append('(' + l + ')' + r)
        dp[i] = cur

    return dp[n]


print(generateParenthesis_dp(3))
