class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        nums = []
        i, j, k = 0, 0, 0
        while i < len(nums1) and j < len(nums2):
            cur1 = nums1[i]
            cur2 = nums2[j]

            if cur1 == cur2:
                nums.append(cur1)
                k += 1
                i += 1
                j += 1
            elif cur1 < cur2:
                i += 1
            else:
                j += 1
        return nums[0:k]


s = Solution()
res = s.intersect([1, 2, 3], [2, 3])
print(res)
