class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        类比成爬楼，只不过有限制条件
        """
        if s[0] == '0':
            return 0
        pre, cur = 1, 1
        for i in range(1, len(s)):
            temp = cur
            if s[i] == '0':
                # 只满足一种情况，类比爬楼梯，只能一次爬两层，所以不增加次数，dp[i] = dp[i-2]
                if s[i - 1] == '1' or s[i - 1] == '2':
                    cur = pre
                else:
                    return 0
            # 满足两种情况，可以走一阶也可以走两阶，所以dp[i]=dp[i-1]+dp[i-2]
            elif ('1' <= s[i] <= '6' and (s[i - 1] == '2')) or s[i - 1] == '1':
                cur += pre
            pre = temp
        return cur


if __name__ == '__main__':
    s = Solution().numDecodings('17')
    print(s)
