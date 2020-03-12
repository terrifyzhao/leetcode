class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        num_sum = sum(A) // 3
        if sum(A) % 3 != 0:
            return False

        tmp_sum = 0
        count = 0
        for i in range(len(A)):
            tmp_sum += A[i]
            if tmp_sum == num_sum:
                count += 1
                tmp_sum = 0
            if count == 3:
                return True
        return False


Solution().canThreePartsEqualSum([10, -10, 10, -10, 10, -10, 10, -10])
