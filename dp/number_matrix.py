class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        row = len(matrix)
        col = len(matrix[0]) if row else 0
        self.dp = [[0 for _ in range(col + 1)] for _ in range(row + 1)]

        for i in range(row):
            for j in range(col):
                self.dp[i + 1][j + 1] = self.dp[i + 1][j] + \
                                        self.dp[i][j + 1] + \
                                        self.matrix[i][j] - \
                                        self.dp[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.dp[row2+1][col2+1] - self.dp[row1][col2+1] - self.dp[row2+1][col1] + self.dp[row1][col1]
