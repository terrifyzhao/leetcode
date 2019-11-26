class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int

        自顶向下
        """
        if len(triangle) == 1:
            return triangle[0][0]
        triangle[1][0] = triangle[0][0] + triangle[1][0]
        triangle[1][1] = triangle[0][0] + triangle[1][1]
        for i in range(2, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] = triangle[i - 1][j] + triangle[i][j]
                elif 0 < j < len(triangle[i]) - 1:
                    triangle[i][j] = min(triangle[i - 1][j - 1], triangle[i - 1][j]) + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] = triangle[i - 1][j - 1] + triangle[i][j]
        return min(triangle[-1][:])

    def minimumTotal2(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int

        自底向上
        """
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i]) - 1, -1, -1):
                triangle[i][j] = min(triangle[i + 1][j], triangle[i + 1][j + 1]) + triangle[i][j]
        return triangle[0][0]


if __name__ == '__main__':
    a = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    s = Solution().minimumTotal2(a)
    print(s)
