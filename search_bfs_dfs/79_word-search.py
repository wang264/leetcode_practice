# 79. Word Search
# Medium
#
# Given an m x n board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or
# vertically neighboring. The same letter cell may not be used more than once.
#
# Example 1:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
#
# Example 2:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
#
# Example 3:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
#
#
# Constraints:
# * m == board.length
# * n = board[i].length
# * 1 <= m, n <= 200
# * 1 <= word.length <= 103
# * board and word consists only of lowercase and uppercase English letters.

from typing import List


class Solution:
    deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        # pick starting point
        for i in range(rows):
            for j in range(cols):
                visited = set()
                visited.add((i,j))
                if self.dfs_helper(board, word, 0, i, j, visited):
                    return True
        return False

    def dfs_helper(self, board, word, curr_idx, row, col, visited):

        if board[row][col] == word[curr_idx]:
            if curr_idx == len(word) - 1:
                return True

            for d_row, d_col in Solution.deltas:
                next_row, next_col = row + d_row, col + d_col
                if self.has_visit_that_location(next_row, next_col, visited):
                    continue
                if not self.is_valid_location(board, next_row, next_col):
                    continue

                visited.add((next_row, next_col))
                curr_idx += 1
                if self.dfs_helper(board, word, curr_idx, next_row, next_col, visited):
                    return True
                curr_idx -= 1
                visited.remove((next_row, next_col))
            return False
        else:
            return False

    def has_visit_that_location(self, row, col, visited):
        if (row, col) in visited:
            return True
        else:
            return False

    def is_valid_location(self, board, row, col):
        if 0 <= row < len(board) and 0 <= col < len(board[0]):
            return True
        else:
            return False


sol = Solution()
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
# board = [["A","B","C"]]
# word = "ABC"
sol.exist(board, word)
