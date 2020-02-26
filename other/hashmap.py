class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
        self.store = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        # 如果包含
        if val in self.data.keys():
            return False
        self.store.append(val)
        self.data[val] = val
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.data.keys():
            self.data.pop(val)
            self.store.remove(val)
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        return self.store[random.randint(0, len(self.store) - 1)]




obj = RandomizedSet()
param_1 = obj.insert(0)
param_2 = obj.insert(0)
param_3 = obj.insert(2)
param_8 = obj.getRandom()
param_4 = obj.insert(3)
param_5 = obj.remove(1)
param_6 = obj.insert(3)
param_7 = obj.insert(2)
param_8 = obj.getRandom()

print(param_1)
print(param_2)
print(param_3)
print(param_4)
print(param_5)
print(param_6)
# print(param_7)
