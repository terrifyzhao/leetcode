class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def dfs(path, begin, target):

            if target == 0:
                res.append(list(path))
                return

            for i in range(begin, len(candidates)):
                if candidates[i] > target:
                    break
                if i > begin and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                dfs(path, begin + 1, target - candidates[i])
                path.pop()

        res = []
        candidates.sort()
        dfs([], 0, target)
        return res
