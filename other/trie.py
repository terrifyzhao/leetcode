class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.item = ''


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for i in list(word):
            if not node.children[ord(i) - ord('a')]:
                node.children[ord(i) - ord('a')] = TrieNode()
            node = node.children[ord(i) - ord('a')]
        node.item = word

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for i in list(word):
            if not node.children[ord(i) - ord('a')]:
                return False
            node = node.children[ord(i) - ord('a')]
        return node.item == word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for i in list(prefix):
            if not node.children[ord(i) - ord('a')]:
                return False
            node = node.children[ord(i) - ord('a')]
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('word')
obj.insert('add')
param_2 = obj.search('word')
param_3 = obj.startsWith('ad')
param_4 = obj.startsWith('word')

print(param_2)
print(param_3)
print(param_4)
