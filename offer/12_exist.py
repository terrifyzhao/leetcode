class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row = len(board)
        column = len(board[0])

        def bfs(i, j, k):
            has_path = False
            if 0 <= i < row and 0 <= j < column and word[k] == board[i][j]:
                if k == len(word) - 1:
                    return True
                tmp, board[i][j] = board[i][j], '*'
                has_path = bfs(i - 1, j, k + 1) or \
                           bfs(i, j - 1, k + 1) or \
                           bfs(i + 1, j, k + 1) or \
                           bfs(i, j + 1, k + 1)
                if not has_path:
                    board[i][j] = tmp

            return has_path

        for i in range(row):
            for j in range(column):
                if bfs(i, j, 0):
                    return True
        return False
