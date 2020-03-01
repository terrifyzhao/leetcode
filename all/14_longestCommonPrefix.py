class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        length = min([len(s) for s in strs])
        res = ''
        for j in range(length):
            tmp_s = strs[0][j]
            for str in strs[1:]:
                s = str[j]
                if tmp_s != s:
                    return res
            res += tmp_s

        return res
