"""Given an m x n grid of characters board and a string word,
return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once."""


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        def backtrack(i: int, j: int, k: int) -> bool:
            if k == len(word): return True
            # check if i or j is out of bounds or the current char is different from the corresponding char of word
            # this condition also covers for the visited char case
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
                return False
            char = board[i][j]
            # mark as visited
            board[i][j] = ''
            # check recursively for the sequentially adjacent cells
            if (backtrack(i - 1, j, k + 1) or backtrack(i + 1, j, k + 1) or
                    backtrack(i, j + 1, k + 1) or backtrack(i, j - 1, k + 1)):
                return True
            board[i][j] = char
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False


solution = Solution()
is_exist = solution.exist(board=[["A", "B", "C", "E"],
                                 ["S", "F", "C", "S"],
                                 ["A", "D", "E", "E"]],
                          word='ABCCED')
print(is_exist)
