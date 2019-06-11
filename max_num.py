class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not nums:
            return ''
        from functools import cmp_to_key
        res = sorted(map(str, nums), key=cmp_to_key(lambda x, y: (int(y + x)) - (int(x + y))))
        return ''.join(res) if res[0] != '0' else '0'


s = Solution()
r = s.largestNumber([3, 30, 34, 5, 9])
print(r)
