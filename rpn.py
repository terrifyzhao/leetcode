class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for s in tokens:
            if s != "+" and s != '-' and s != '*' and s != '/':
                stack.append(int(s))
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                c = 0
                if s == '+':
                    c = a + b
                elif s == '-':
                    c = b - a
                elif s == '*':
                    c = a * b
                elif s == '/':
                    c = int(b / a)
                stack.append(c)
        return stack[0]


s = Solution()
res = s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
print(res)

