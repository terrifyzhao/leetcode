class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def dfs(cur, begin, target):
            if target < 0:
                return
            if target == 0:
                res.append(list(cur))
                return

            for i in range(begin, len(candidates)):
                cur.append(candidates[i])
                dfs(cur, i, target - candidates[i])
                cur.pop()

        res = []
        candidates.sort()
        dfs([], 0, target)
        return res


print(Solution().combinationSum([2, 3, 6, 7], 7))
