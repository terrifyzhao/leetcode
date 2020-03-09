class Solution(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """

        visited = [[False for _ in range(n)] for _ in range(m)]

        def valid_num(num):
            num_sum = 0
            while num:
                num, m = divmod(num, 10)
                num_sum += m
            return num_sum

        def dfs(i, j, visited):
            count = 0
            if 0 <= i < m and 0 <= j < n and valid_num(i) + valid_num(j) <= k and not visited[i][j]:
                visited[i][j] = True
                count = dfs(i + 1, j, visited) + \
                        dfs(i, j + 1, visited) + \
                        1

            return count

        count = dfs(0, 0, visited)
        return count
