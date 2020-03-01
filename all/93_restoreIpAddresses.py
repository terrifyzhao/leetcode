# class Solution(object):
#     def restoreIpAddresses(self, s):
#         """
#         :type s: str
#         :rtype: List[str]
#         """
#         res = []
#         n = len(s)
#
#         def is_ip(ip_str):
#
#             if not ip_str or (len(ip_str) > 1 and ip_str[0] == '0') or int(ip_str) > 255:
#                 return False
#             return True
#
#         for i in range(4):
#             for j in range(i + 1, i + 4):
#                 for k in range(j + 1, j + 4):
#                     if i < n and j < n and k < n:
#                         s1 = s[:i + 1]
#                         s2 = s[i + 1:j + 1]
#                         s3 = s[j + 1:k + 1]
#                         s4 = s[k + 1:]
#
#                         if all(map(is_ip, [s1, s2, s3, s4])):
#                             res.append('.'.join([s1, s2, s3, s4]))
#         return res

class Solution:
    def restoreIpAddresses2(self, s):
        res = []
        n = len(s)

        def backtrack(i, tmp, flag):
            if i == n and flag == 0:
                res.append(tmp[:-1])
                return
            if flag < 0:
                return
            for j in range(i, i + 3):
                if j < n:
                    # 首元素而且是0
                    if i == j and s[j] == "0":
                        backtrack(j + 1, tmp + s[j] + ".", flag - 1)
                        break

                    # 合法数组
                    if 0 < int(s[i:j + 1]) <= 255:
                        backtrack(j + 1, tmp + s[i:j + 1] + ".", flag - 1)

        backtrack(0, "", 4)
        return res

    def restoreIpAddresses(self, s):
        res = []
        n = len(s)

        def dfs(i, tmp, target):
            if i == n and target == 0:
                res.append(tmp[:-1])
            if target < 0:
                return

            for j in range(i, i + 3):
                if j < n:
                    if j == i and s[j] == '0':
                        dfs(j + 1, tmp + s[j] + '.', target - 1)
                        break
                    if 0 < int(s[i:j + 1]) <= 255:
                        dfs(j + 1, tmp + s[i:j + 1] + '.', target - 1)

        dfs(0, '', 4)
        return res


a = Solution().restoreIpAddresses("25525511135")
print(a)
