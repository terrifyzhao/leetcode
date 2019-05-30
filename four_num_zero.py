class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        dic = {}
        for a in A:
            for b in B:
                num = a + b
                dic[num] = dic.get(num, 0) + 1

        res = 0
        for c in C:
            for d in D:
                num = -c - d
                if dic.get(num, 0):
                    res += 1
        return res
