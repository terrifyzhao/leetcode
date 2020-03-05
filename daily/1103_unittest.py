class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        res = [0 for _ in range(num_people)]

        i = 0
        while candies > 0:
            res[i % num_people] += min(i + 1, candies)
            candies -= min(i + 1, candies)
            i += 1
        return res


print(Solution().distributeCandies(7, 4))
