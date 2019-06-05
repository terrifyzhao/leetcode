import heapq


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        height = []
        res = []

        # 先把所有坐标点添加到一个数组里，如果是左边的点就把高度设置为负数
        for building in buildings:
            height.append((building[0], -building[2]))
            height.append((building[1], building[2]))

        height = sorted(height, key=lambda x: x[0])

        pq = []
        # 添加地平线
        heapq.heappush(pq, 0)
        # 上一次的最大值
        prev = 0

        for h in height:
            # 左上角
            if h[1] < 0:
                # 大根堆，所以不用加负号
                heapq.heappush(pq, h[1])
            else:
                pq.remove(-h[1])
                heapq.heapify(pq)

            # 当前最大高度
            cur = pq[0]

            # 如果当前的最大高度和之前的不一样，说明前一个最大高度被移除了，或者有更高的building加入
            if cur != prev:
                res.append([h[0], -cur])
                prev = cur
        return res


if __name__ == '__main__':
    b = [[0,2,3],[2,5,3]]

    s = Solution()
    res = s.getSkyline(b)
    print(res)
