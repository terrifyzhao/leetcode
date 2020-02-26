# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return None
        add = 0
        head = ListNode(0)
        pre = head
        while l1 or l2:
            if l1 and not l2:
                add, val = divmod(l1.val + add, 10)
                l1 = l1.next
            elif not l1 and l2:
                add, val = divmod(l2.val + add, 10)
                l2 = l2.next
            else:
                add, val = divmod(l1.val + l2.val + add, 10)
                l1 = l1.next
                l2 = l2.next
            cur = ListNode(val)
            pre.next = cur
            pre = cur
        if add != 0:
            pre.next = ListNode(add)
        return head.next


l1 = ListNode(7)
l1.next = ListNode(3)
# l1.next.next = ListNode(3)

l2 = ListNode(1)
l2.next = ListNode(7)
# l2.next.next = ListNode(4)

a = Solution().addTwoNumbers(l1, l2)
while a:

    print(a.val)
    a = a.next
