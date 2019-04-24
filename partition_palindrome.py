import pysnooper


class Solution:
    @pysnooper.snoop()
    def _partition(self, s, index, t, result):
        if index == len(s):
            result.append(t.copy())
            return

        for i in range(index + 1, len(s) + 1):
            if s[index:i] == s[index:i][::-1]:
                t.append(s[index:i])
                self._partition(s, i, t, result)
                t.pop()

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = list()
        if not s:
            return result

        self._partition(s, 0, list(), result)
        return result


s = Solution()
res = s.partition('aab')
print(res)

# a = [1, 2, 3]
# b = a[::-1]
# print(b)
