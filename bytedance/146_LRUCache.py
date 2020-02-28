from collections import deque


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.index = deque()
        self.dic = {}
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.index:
            self.index.remove(key)
            self.index.append(key)

        return self.dic.get(key, -1)

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.index:
            self.index.remove(key)
            self.index.append(key)

        else:
            if len(self.index) == self.capacity:
                top_key = self.index.popleft()
                del self.dic[top_key]
            self.index.append(key)

        self.dic[key] = value



# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
obj.get(1)
obj.put(3, 3)
obj.get(2)
obj.put(4, 4)
obj.get(1)
obj.get(3)
obj.get(4)
