class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        # 如果不把负号取出来，取余数的时候会出问题
        sign = '-' if numerator * denominator < 0 else ''
        numerator, denominator = abs(numerator), abs(denominator)
        m, n = divmod(numerator, denominator)
        int_part = str(m)
        if not n:
            return sign + int_part
        decimal_part = []
        dic = {}
        i = 0
        while n and n not in dic:
            dic[n] = i
            i += 1
            m, n = divmod(n * 10, denominator)
            decimal_part.append(str(m))
        if n:
            decimal_part.insert(dic[n], '(')
            decimal_part.append(')')
        return sign + int_part + '.' + ''.join(decimal_part)


s = Solution()
res = s.fractionToDecimal(-50, 8)
print(res)
