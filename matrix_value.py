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
        first_row = matrix[0]
        index_row = 0
        for num in first_row:
            if target > num:
                index_row += 1
            else:
                break

        column = [row[index_row] for row in matrix]
        for num in column:
            if num == target:
                return True

        return False


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
