class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if not s1:
            return True
        if not s2:
            return False
        dic = {}
        for s in s1:
            dic[s] = dic.get(s, 0) + 1

        start = 0
        match = 0
        for i in range(len(s2)):
            s = s2[i]
            if s in dic:
                dic[s] -= 1
                if dic[s] == 0:
                    match += 1

            if match == len(dic):
                return True

            if i >= len(s1) - 1:
                tmp_s = s2[start]
                start += 1
                if tmp_s in dic:
                    if dic[tmp_s] == 0:
                        match -= 1
                    dic[tmp_s] += 1
        return False


if __name__ == '__main__':
    a = Solution().checkInclusion("abcdxabcde", "abcdeabcdx")
    print(a)
