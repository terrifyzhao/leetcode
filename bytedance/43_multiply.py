class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            n1 = ord(num1[i]) - ord('0')
            for j in range(len(num2) - 1, -1, -1):
                n2 = ord(num2[j]) - ord('0')
                s = res[i + j + 1] + n1 * n2
                res[i + j + 1] = s % 10
                res[i + j] += s // 10

        res = [str(r) for r in res]
        while len(res) > 1 and res[0] == '0':
            res = res[1:]

        return ''.join(res)
