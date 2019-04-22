# search value of matrix

# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        column = len(matrix[0]) - 1
        row = 0
        while True:
            if column < 0 or row > len(matrix) - 1:
                return False

            if matrix[row][column] == target:
                return True
            elif matrix[row][column] > target:
                column -= 1
            elif matrix[row][column] < target:
                row += 1


s = Solution()
a = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
res = s.searchMatrix(a, 20)
print(res)
