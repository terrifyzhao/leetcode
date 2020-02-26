class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        num = 0
        op = '+'
        stack = []
        for i, c in enumerate(list(s)):
            # 判断是否是数字
            if ord(c) >= ord('0'):
                num = num * 10 + ord(c) - ord('0')
            # 判断是否是符号，或者是最后一个符号，是的话就根据上一轮保存的op进行计算
            if (ord(c) < ord('0') and c != ' ') or i == len(s) - 1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    tmp = stack[-1] * num
                    stack.pop()
                    stack.append(tmp)
                elif op == '/':
                    tmp = int(stack[-1] / num)
                    stack.pop()
                    stack.append(tmp)
                op = c
                num = 0
        while len(stack) > 0:
            res += stack.pop()
        return res


s = Solution()
string = " 14-3/2 "
res = s.calculate(string)
print(res)
