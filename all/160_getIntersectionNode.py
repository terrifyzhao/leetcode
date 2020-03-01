# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        n1 = headA
        n2 = headB
        while n1 != n2:
            n1 = n1.next if n1 else headB
            n2 = n2.next if n2 else headA
        return n1


l1 = ListNode(7)
l1.next = ListNode(8)

Solution().getIntersectionNode(l1)
