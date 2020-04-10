class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1 = len(nums1)
        n2 = len(nums2)
        left = (n1 + n2 + 1) // 2
        right = (n1 + n2 + 2) // 2

        return (self.findK(nums1, 0, n1 - 1, nums2, 0, n2 - 1, left) +
                self.findK(nums1, 0, n1 - 1, nums2, 0, n2 - 1, right)) * 0.5

    def findK(self, nums1, start1, end1, nums2, start2, end2, k):
        len1 = end1 - start1 + 1
        len2 = end2 - start2 + 1
        if len1 > len2:
            return self.findK(nums2, start2, end2, nums1, start1, end1, k)
        if len1 == 0:
            return nums2[start2 + k - 1]
        if k == 1:
            return min(nums1[start1], nums2[start2])

        i = start1 + min(len1, k // 2) - 1
        j = start2 + min(len2, k // 2) - 1

        if nums1[i] > nums2[j]:
            return self.findK(nums1, start1, end1, nums2, j + 1, end2, k - (j - start2 + 1))
        else:
            return self.findK(nums1, i + 1, end1, nums2, start2, end2, k - (i - start1 + 1))
