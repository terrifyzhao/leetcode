# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        while not head or not head.next:
            return head
        p = head
        tmp = head.next
        q = head.next
        while q and q.next:
            p.next = q.next
            p = q.next
            q.next = p.next
            q = p.next
        p.next = tmp
        return head


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    s = Solution()
    print(s.oddEvenList(head))
