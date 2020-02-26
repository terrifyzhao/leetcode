import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num_dic = {}

        for num in nums:
            num_dic[num] = num_dic.get(num, 0) + 1

        heap = []
        for v in num_dic.items():
            heapq.heappush(heap, (-v[1], v[0]))

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res


s = Solution()
nums = [4, 1, -1, 2, -1, 2, 3]
# nums = [1, 2]
k = 2
r = s.topKFrequent(nums, k)
print(r)
