# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        length = 0
        p = head
        while p:
            length += 1
            p = p.next

        if length == 2:
            return head.val == head.next.val
        if length == 3:
            return head.val == head.next.next.val

        q = head
        for i in range(int((length + 2 - 1) / 2)):
            q = q.next

        p = head
        k = head.next
        head.next = None

        for i in range(int(length / 2) - 1):
            j = k.next
            k.next = p
            p = k
            k = j
        while p and q:
            if p.val != q.val:
                return False
            p = p.next
            q = q.next
        return True


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    # head.next.next = ListNode(0)
    s = Solution()
    print(s.isPalindrome(head))
