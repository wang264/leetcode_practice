# 51. N-Queens
# Hard
#
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle.
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
#
#
# Example 1:
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
#
# Example 2:
# Input: n = 1
# Output: [["Q"]]
#
# Constraints:
# 1 <= n <= 9

from typing import List


class Solution:

    def solveNQueens(self, n: int) -> List[List[str]]:
        # write your code here
        # curr_col_permutation: 用來記錄每一個Queen的Column, Row默認從0，1，2，3....
        # visited 用來記錄幫助判斷擺放是否合理。列數和行數之和 列數和行數之差，用來判斷是否會
        # 斜綫攻擊。
        rslt = []
        visited = {'col_num': set(), 'row_col_sum': set(), 'row_col_diff': set()}
        self.dfs_helper(n, [], visited, rslt)
        return rslt

    def dfs_helper(self, n, curr_col_permutation, visited, boards):
        if len(curr_col_permutation) == n:
            boards.append(self.draw(curr_col_permutation))
            return

        row = len(curr_col_permutation)
        # try possible column indexes
        for col in range(n):
            if not self.is_valid(col, row, visited):
                continue
            curr_col_permutation.append(col)
            visited['col_num'].add(col)
            visited['row_col_sum'].add(row + col)
            visited['row_col_diff'].add(row - col)
            self.dfs_helper(n, curr_col_permutation, visited, boards)
            visited['col_num'].remove(col)
            visited['row_col_sum'].remove(row + col)
            visited['row_col_diff'].remove(row - col)
            curr_col_permutation.pop()

    def is_valid(self, col, row, visited):
        if col in visited['col_num']:
            return False
        if row + col in visited['row_col_sum']:  # 斜綫，y=x+k
            return False
        if row - col in visited['row_col_diff']:  # 斜綫 y=-x+k
            return False
        return True

    def draw(self, permutation):
        board = []
        n = len(permutation)
        for col in permutation:
            row_string = ''.join(['Q' if c == col else '.' for c in range(n)])
            board.append(row_string)
        return board


sol = Solution()

assert sol.solveNQueens(n=1) == [['Q']]

assert sol.solveNQueens(n=2) == []
