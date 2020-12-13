# 37. Sudoku Solver
# Hard
#
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# A sudoku solution must satisfy all of the following rules:
# 1.Each of the digits 1-9 must occur exactly once in each row.
# 2.Each of the digits 1-9 must occur exactly once in each column.
# 3.Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.
#
# Example 1:
#
#
# Input: board = [["5","3",".",".","7",".",".",".","."],
#                 ["6",".",".","1","9","5",".",".","."],
#                 [".","9","8",".",".",".",".","6","."],
#                 ["8",".",".",".","6",".",".",".","3"],
#                 ["4",".",".","8",".","3",".",".","1"],
#                 ["7",".",".",".","2",".",".",".","6"],
#                 [".","6",".",".",".",".","2","8","."],
#                 [".",".",".","4","1","9",".",".","5"],
#                 [".",".",".",".","8",".",".","7","9"]]
#
# Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
# Explanation: The input board is shown above and the only valid solution is shown below:
#
# Constraints:
#
# * board.length == 9
# * board[i].length == 9
# * board[i][j] is a digit or '.'.
# * It is guaranteed that the input board has only one solution.
#


# 对于这道题目来说，我们要明确几点
# 1.目标(base case) ：填满每个格子。
# 2.选择列表(choice list)：每个空的格子可以填入1-9这九个数字。
# 3.约束条件(constrain)：1-9在每一行、每一列和每个3x3的大格中都只能出现一次。
# 4.选择路径(path)：由于我们是inplace操作，board就存储了已经做过的选择。
#
# 我们在这里设置backtrack函数的返回类型为bool，这样一来，当程序找到可行解后就能终止递归。

# 算法流程
# 从最左上角的方格开始，即i = 0, j = 0，开始一行一行填充。

# corner case：
# 1.如果j = 9，说明越界，从下一行的第0列开始填。
# 2.如果i = 9，说明找到可行解，返回True。
# 3.如果`boardi != 0，这个格子不需要我们填，于是去填下一个格子。

# 从1到9迭代循环数组，尝试放置数字val进入(i, j)的格子。
# 1.如果符合约束条件：
# 2.将val放置在(i, j)的格子中。
# 3.进行dfs，对后面的格子进行相同的操作。
# 4.判断是否能找出数独的解。如果可以，返回True。
# 5.进行回溯，即将(i, j)恢复为0。

# 如果遍历完1-9都没有找到数独的解，返回False。
#
# 复杂度分析
# 时间复杂度：时间复杂度是常数。由于数独的大小是固定的，因此没有 N 变量来衡量。上限是
# (9!)^9。对第一行来说，第一个格子不会超过9种情况，第二个格子不会超过8种...所以第一行不会超过
# 9!个情况。那么所有行不会超过
# (9!)^2
# 空间复杂度：数独大小固定，空间用来存储数独，行，列和子方块的结构，每个有 81 个元素。


from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.back_track(board, 0, 0)
        return board

    def back_track(self, board, i, j):
        m, n = 9, 9
        # 到达第n列，越界，换到下一行第0列重新开始
        if j == n:
            return self.back_track(board, i + 1, 0)
        # 到达第m行，说明找到可行解，触发 base case
        if i == m:
            return True
        # 如果有预设数字，不用我们穷举
        if board[i][j] != '.':
            return self.back_track(board, i, j + 1)

        for val in range(1, 10):
            # 如果遇到不合法的数字，就跳过
            if not self.isValid(board, i, j, val):
                continue
            # 添加选择
            board[i][j] = str(val)
            # 如果找到一个可行解，立即结束
            if self.back_track(board, i, j + 1):
                return True
            # 撤回选择
            board[i][j] = '.'
        # 穷举完1~9，依然没有找到可行解，此路不通
        return False

    def isValid(self, board, row, col, val):
        for i in range(9):
            # 判断行是否存在重复
            if board[row][i] == str(val):
                return False
            # 判断列是否存在重复
            if board[i][col] == str(val):
                return False
            # 判断 3 x 3 方框是否存在重复
            if board[row // 3 * 3 + i // 3][col // 3 * 3 + i % 3] == str(val):
                return False
        return True


import numpy as np

sol = Solution()
board = np.array(
    [["5", "3", ".", ".", "7", ".", ".", ".", "."],
     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
     [".", "9", "8", ".", ".", ".", ".", "6", "."],
     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
     [".", "6", ".", ".", ".", ".", "2", "8", "."],
     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
     [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
sol.solveSudoku(board=board)
board
