class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        count = 0
        n = len(M)
        visited = [0] * n

        def dfs(visited, i):
            for j in range(n):
                if M[i][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    dfs(visited, j)

        for i in range(n):
            if visited[i] == 0:
                dfs(visited, i)
                count += 1
        return count
