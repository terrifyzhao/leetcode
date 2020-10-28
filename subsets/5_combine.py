class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        def dfs(cur, begin):
            if len(cur) == k:
                res.append(list(cur))
                return

            for i in range(begin, n + 1):
                cur.append(i)
                dfs(cur, i + 1)
                cur.pop()

        res = []
        dfs([], 1)
        return res


print(Solution().combine(4, 2))
