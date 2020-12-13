# 212. Word Search II
# Hard
#
# Given an m x n board of characters and a list of strings words, return all words on the board.
# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally
# or vertically neighboring. The same letter cell may not be used more than once in a word.
#
# Example 1:
# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
#
# Example 2:
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []

from typing import List


class Solution:
    deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rslt = []
        max_word_length = max(len(w) for w in words)

        rows = len(board)
        cols = len(board[0])
        # pick starting point
        for i in range(rows):
            for j in range(cols):
                visited = set()
                visited.add((i, j))
                self.dfs_helper(board, words, board[i][j], i, j, visited, rslt, max_word_length)
        return rslt

    def dfs_helper(self, board, words, curr_word, row, col, visited, rslt, max_word_length):
        if len(curr_word) > max_word_length:
            return
        if curr_word in words and curr_word not in rslt:
            rslt.append(curr_word)

        for d_row, d_col in Solution.deltas:
            next_row, next_col = row + d_row, col + d_col
            if self.has_visit_that_location(next_row, next_col, visited):
                continue
            if not self.is_valid_location(board, next_row, next_col):
                continue

            visited.add((next_row, next_col))
            curr_word = curr_word+board[next_row][next_col]
            self.dfs_helper(board, words, curr_word, next_row, next_col, visited, rslt, max_word_length)
            # pop the last character
            curr_word = curr_word[0:-1]
            visited.remove((next_row, next_col))

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
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
sol.findWords(board,words)

sol = Solution()
board = [["a"]]
words = ["a"]
sol.findWords(board,words)