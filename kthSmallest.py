import heapq


# 堆
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = []
        for row in matrix:
            for v in row:
                heapq.heappush(heap, -v)
                if len(heap) > k:
                    heapq.heappop(heap)
        # for i in range(k-1):

        return -heap[0]


# 二分
class BiSolution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        row = len(matrix)
        col = len(matrix[0])
        left = matrix[0][0]
        right = matrix[-1][-1]
        while left <= right:
            mid = int((right - left) / 2 + left)
            count = 0
            for i in range(row):
                for j in range(col):
                    if matrix[i][j] <= mid:
                        count += 1
                    else:
                        break
            if count < k:
                left = mid + 1
            else:
                right = mid - 1
        return left

s = BiSolution()
matrix = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]
k = 3
res = s.kthSmallest(matrix, k)
print(res)
