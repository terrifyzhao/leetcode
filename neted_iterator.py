class NestedInteger(object):
    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nums = []
        self.nums2 =[]

        def dfs(data):
            for v in data[-1::]:
                if v.isInteger():
                    self.nums.append(v.getInteger())
                else:
                    dfs(v.getList())

        dfs(nestedList)
        while self.nums:
            self.nums2.append(self.nums.pop())

    def next(self):
        """
        :rtype: int
        """
        return self.nums.pop()

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.nums) > 0:
            return True
        return False


i, v = NestedIterator([[1, 1], 2, [1, 1]]), []
while i.hasNext():
    v.append(i.next())
print(v)
