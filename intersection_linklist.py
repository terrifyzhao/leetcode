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
        if headA is None or headB is None:
            return None
        a = headA
        b = headB
        len_a = 0
        len_b = 0
        while a:
            len_a += 1
            a = a.next
        while b:
            len_b += 1
            b = b.next
        a = headA
        b = headB
        step = len_a - len_b
        if len_a - len_b > 0:
            for i in range(step):
                a = a.next
        else:
            for i in range(step*-1):
                b = b.next
        while a is not b:
            a = a.next
            b = b.next
            if a is None or b is None:
                return None
        return a


node1 = ListNode(4)
head1 = node1
node1.next = ListNode(1)
node1 = node1.next
node1.next = ListNode(8)
node1 = node1.next
node1.next = ListNode(4)
node1 = node1.next
node1.next = ListNode(5)

node2 = ListNode(5)
head2 = node2
node2.next = ListNode(0)
node2 = node2.next
node2.next = ListNode(1)
node2 = node2.next
node2.next = ListNode(8)
node2 = node2.next
node2.next = ListNode(4)
node2 = node2.next
node2.next = ListNode(5)

s = Solution()
res = s.getIntersectionNode(head1, head2)
print(res)
