class Node(object):
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        # 把新节点插到老节点后面，有几个老节点就插几个新节点
        node = head
        while node:
            new_node = Node(node.val)
            new_node.next = node.next
            node.next = new_node
            node = node.next.next

        # 复制random
        node = head
        while node:
            if node.random:
                node.next.random = node.random.next
            node = node.next.next

        # 把新节点剥离出来
        node = head
        new_head = head.next
        while node:
            new_node = node.next
            node.next = new_node.next
            if new_node.next:
                new_node.next = node.next.next
            node = node.next
        return new_head
