class TrieNode:

    def __init__(self):
        self.children = {}
        self.item = ''


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # self.root = TrieNode()
        self.root = [None] * 27
        self.item = ''

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for i in word:
            if not node[ord(i) - ord('a')]:
                node[ord(i) - ord('a')] = [None] * 27
            node = node[ord(i) - ord('a')]
        node[26] = word

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for i in word:
            if not node[ord(i) - ord('a')]:
                return False
            node = node[ord(i) - ord('a')]
        return node[26] == word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for i in prefix:
            if not node[ord(i) - ord('a')]:
                return False
            node = node[ord(i) - ord('a')]
        return True


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.res = set()
        trie = Trie()
        for word in words:
            trie.insert(word)

        row = len(board)
        column = len(board[0])
        for i in range(row):
            for j in range(column):
                c = board[i][j]
                board[i][j] = 1
                self.find(c, board, i, j, trie)
                board[i][j] = c
        return list(self.res)

    def find(self, cur, board, i, j, trie):
        if trie.search(cur):
            self.res.add(cur)

        if trie.startsWith(cur):
            if i - 1 >= 0 and board[i - 1][j] != 1:
                c = board[i - 1][j]
                board[i - 1][j] = 1
                if trie.startsWith(cur + c):
                    self.find(cur + c, board, i - 1, j, trie)
                board[i - 1][j] = c
            if i + 1 < len(board) and board[i + 1][j] != 1:
                c = board[i + 1][j]
                board[i + 1][j] = 1
                if trie.startsWith(cur + c):
                    self.find(cur + c, board, i + 1, j, trie)
                board[i + 1][j] = c
            if j - 1 >= 0 and board[i][j - 1] != 1:
                c = board[i][j - 1]
                board[i][j - 1] = 1
                if trie.startsWith(cur + c):
                    self.find(cur + c, board, i, j - 1, trie)
                board[i][j - 1] = c
            if j + 1 < len(board[0]) and board[i][j + 1] != 1:
                c = board[i][j + 1]
                board[i][j + 1] = 1
                if trie.startsWith(cur + c):
                    self.find(cur + c, board, i, j + 1, trie)
                board[i][j + 1] = c


if __name__ == '__main__':
    # words = ["oath", "pea", "eat", "rain"]
    # board = [
    #     ['o', 'a', 'a', 'n'],
    #     ['e', 't', 'a', 'e'],
    #     ['i', 'h', 'k', 'r'],
    #     ['i', 'f', 'l', 'v']
    # ]

    # board = [["a", "b"], ["a", "a"]]
    # words = ["aba", "baa", "bab", "aaab", "aaa", "aaaa", "aaba"]

    board = [["b", "a", "a", "b", "a", "b"], ["a", "b", "a", "a", "a", "a"], ["a", "b", "a", "a", "a", "b"],
             ["a", "b", "a", "b", "b", "a"], ["a", "a", "b", "b", "a", "b"], ["a", "a", "b", "b", "b", "a"],
             ["a", "a", "b", "a", "a", "b"]]
    words = ["bbaabaabaaaaabaababaaaaababb", "aabbaaabaaabaabaaaaaabbaaaba", "babaababbbbbbbaabaababaabaaa",
             "bbbaaabaabbaaababababbbbbaaa", "babbabbbbaabbabaaaaaabbbaaab", "bbbababbbbbbbababbabbbbbabaa",
             "babababbababaabbbbabbbbabbba", "abbbbbbaabaaabaaababaabbabba", "aabaabababbbbbbababbbababbaa",
             "aabbbbabbaababaaaabababbaaba", "ababaababaaabbabbaabbaabbaba", "abaabbbaaaaababbbaaaaabbbaab",
             "aabbabaabaabbabababaaabbbaab", "baaabaaaabbabaaabaabababaaaa", "aaabbabaaaababbabbaabbaabbaa",
             "aaabaaaaabaabbabaabbbbaabaaa", "abbaabbaaaabbaababababbaabbb", "baabaababbbbaaaabaaabbababbb",
             "aabaababbaababbaaabaabababab", "abbaaabbaabaabaabbbbaabbbbbb", "aaababaabbaaabbbaaabbabbabab",
             "bbababbbabbbbabbbbabbbbbabaa", "abbbaabbbaaababbbababbababba", "bbbbbbbabbbababbabaabababaab",
             "aaaababaabbbbabaaaaabaaaaabb", "bbaaabbbbabbaaabbaabbabbaaba", "aabaabbbbaabaabbabaabababaaa",
             "abbababbbaababaabbababababbb", "aabbbabbaaaababbbbabbababbbb", "babbbaabababbbbbbbbbaabbabaa"]

    s = Solution()
    res = s.findWords(board, words)
    print(res)
