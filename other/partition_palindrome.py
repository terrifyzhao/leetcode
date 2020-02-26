# partition palindrome

class Solution:

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        self._partition(0, s, [], result)
        return result

    def _partition(self, index, s, tmp, res):
        if index == len(s):
            res.append(tmp.copy())
            return

        for i in range(index + 1, len(s) + 1):
            if s[index:i] == s[index:i][::-1]:
                tmp.append(s[index:i])
                self._partition(i, s, tmp, res)
                tmp.pop()


s = Solution()
res = s.partition('aab')
print(res)

# a = [1, 2, 3]
# b = a[::-1]
# print(b)
