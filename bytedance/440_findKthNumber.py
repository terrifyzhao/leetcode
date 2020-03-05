class Solution(object):

    def find_count(self, prefix, n):
        cur = prefix
        next = cur + 1
        count = 0
        while cur <= n:
            count += min(n + 1, next) - cur
            cur *= 10
            next *= 10
        return count

    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        prefix = 1
        p = 1

        while p < k:
            count = self.find_count(prefix, n)
            # 在当前前缀下，去子树里面找
            if p + count > k:
                prefix *= 10
                p += 1
            # 不在当前前缀
            else:
                # 扩大前缀
                prefix += 1
                # 移到下一个前缀的位置
                p += count
        return prefix
