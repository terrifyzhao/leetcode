class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # self.root = TrieNode()
        self.root = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for i in word:
            node = node.setdefault(i, {})
        node['item'] = word

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for i in word:
            if not node.get(i):
                return False
            node = node.get(i)
        return node.get('item') == word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for i in prefix:
            if not node.get(i):
                return False
            node = node.get(i)
        return True


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.res = set()
        self.trie = Trie()
        for word in words:
            self.trie.insert(word)

        self.row = len(board)
        self.column = len(board[0])
        for i in range(self.row):
            for j in range(self.column):
                if board[i][j] in self.trie.root:
                    self.find('', board, i, j, self.trie.root)

        return list(self.res)

    def find(self, cur, board, i, j, cur_dict):
        cur += board[i][j]
        cur_dict = cur_dict[board[i][j]]

        # 如果找到了就添加到res中
        if 'item' in cur_dict:
            self.res.add(cur)

        # 保护现场
        tmp = board[i][j]
        board[i][j] = '#'

        # 四个方向遍历
        for k in range(4):
            x, y = dx[k] + j, dy[k] + i
            if 0 <= x < self.column and 0 <= y < self.row:
                if board[y][x] != '#' and board[y][x] in cur_dict:
                    self.find(cur, board, y, x, cur_dict)
        # 还原现场
        board[i][j] = tmp


if __name__ == '__main__':
    # words = ["oath", "pea", "eat", "rain"]
    # board = [
    #     ['o', 'a', 'a', 'n'],
    #     ['e', 't', 'a', 'e'],
    #     ['i', 'h', 'k', 'r'],
    #     ['i', 'f', 'l', 'v']
    # ]

    board = [["a", "b"], ["a", "a"]]
    words = ["aba", "baa", "bab", "aaab", "aaa", "aaaa", "aaba"]

    # board = [["a", "b"], ["c", "d"]]
    # words = ["ab", "cb", "ad", "bd", "ac", "ca", "da", "bc", "db", "adcb", "dabc", "abb", "acb"]

    # board = [["b", "a", "a", "b", "a", "b"], ["a", "b", "a", "a", "a", "a"], ["a", "b", "a", "a", "a", "b"],
    #          ["a", "b", "a", "b", "b", "a"], ["a", "a", "b", "b", "a", "b"], ["a", "a", "b", "b", "b", "a"],
    #          ["a", "a", "b", "a", "a", "b"]]
    # words = ["bbaabaabaaaaabaababaaaaababb", "aabbaaabaaabaabaaaaaabbaaaba", "babaababbbbbbbaabaababaabaaa",
    #          "bbbaaabaabbaaababababbbbbaaa", "babbabbbbaabbabaaaaaabbbaaab", "bbbababbbbbbbababbabbbbbabaa",
    #          "babababbababaabbbbabbbbabbba", "abbbbbbaabaaabaaababaabbabba", "aabaabababbbbbbababbbababbaa",
    #          "aabbbbabbaababaaaabababbaaba", "ababaababaaabbabbaabbaabbaba", "abaabbbaaaaababbbaaaaabbbaab",
    #          "aabbabaabaabbabababaaabbbaab", "baaabaaaabbabaaabaabababaaaa", "aaabbabaaaababbabbaabbaabbaa",
    #          "aaabaaaaabaabbabaabbbbaabaaa", "abbaabbaaaabbaababababbaabbb", "baabaababbbbaaaabaaabbababbb",
    #          "aabaababbaababbaaabaabababab", "abbaaabbaabaabaabbbbaabbbbbb", "aaababaabbaaabbbaaabbabbabab",
    #          "bbababbbabbbbabbbbabbbbbabaa", "abbbaabbbaaababbbababbababba", "bbbbbbbabbbababbabaabababaab",
    #          "aaaababaabbbbabaaaaabaaaaabb", "bbaaabbbbabbaaabbaabbabbaaba", "aabaabbbbaabaabbabaabababaaa",
    #          "abbababbbaababaabbababababbb", "aabbbabbaaaababbbbabbababbbb", "babbbaabababbbbbbbbbaabbabaa"]

    s = Solution()
    res = s.findWords(board, words)
    print(res)

