# class Solution(object):
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#         l1 = len(nums1)
#         l2 = len(nums2)
#
#         if l1 and not l2:
#             if l1 ^ 1 == 0:
#                 return nums1[l1 // 2]
#             else:
#                 return (nums1[l1 // 2] + nums1[l1 // 2 + 1]) / 2
#
#         i = 0
#         j = 0
#         length = l1 + l2
#         k = length // 2
#
#         while i + j != k - 2:
#             if nums1[i] < nums2[j]:
#                 i += 1
#             else:
#                 j += 1
#         if length ^ 1 == 0:
#             return min(nums1[i], nums2[j])
#         else:
#
