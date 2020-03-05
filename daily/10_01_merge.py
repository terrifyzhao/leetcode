class Solution(object):
    def merge(self, A, m, B, n):
        """
        :type A: List[int]
        :type m: int
        :type B: List[int]
        :type n: int
        :rtype: None Do not return anything, modify A in-place instead.
        """
        i = m - 1
        j = n - 1
        last = m + n - 1
        while j >= 0:
            if i < 0:
                A[0:j + 1] = B[0:j + 1]
                break
            elif A[i] > B[j]:
                A[last] = A[i]
                i -= 1
            else:
                A[last] = B[j]
                j -= 1
            last -= 1


a = Solution().merge([2, 0],
                     1,
                     [1],
                     1)
print(a)
