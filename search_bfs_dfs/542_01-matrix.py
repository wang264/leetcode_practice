# 542. 01 Matrix
# Medium
#
# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
# The distance between two adjacent cells is 1.
#
# Example 1:
# Input:
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]
#
# Output:
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]
#
# Example 2:
# Input:
# [[0,0,0],
#  [0,1,0],
#  [1,1,1]]
#
# Output:
# [[0,0,0],
#  [0,1,0],
#  [1,2,1]]
#
# Note:
# The number of elements of the given matrix will not exceed 10,000.
# There are at least one 0 in the given matrix.
# The cells are adjacent in only four directions: up, down, left and right.

from collections import deque
from typing import List


class Solution:
    DELTAS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])

        q = deque()
        rslt = [[None] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    rslt[i][j] = 0
                    q.append((i, j))

        distance = 1
        while q:
            for _ in range(len(q)):
                curr_row, curr_col = q.popleft()
                for d_row, d_col in Solution.DELTAS:
                    next_row = curr_row + d_row
                    next_col = curr_col + d_col
                    # valid location and never visit before
                    if self.is_valid(matrix, next_row, next_col) and (not self.visited(rslt, next_row, next_col)):
                        rslt[next_row][next_col] = distance
                        q.append((next_row, next_col))
            distance += 1

        return rslt

    def visited(self, result_matrix, row, col):
        return result_matrix[row][col] is not None

    def is_valid(self, matrix, row, col):
        rows = len(matrix)
        cols = len(matrix[0])
        return 0 <= row < rows and 0 <= col < cols


sol =Solution()
mat = [[0,0,0],
       [0,1,0],
       [1,1,1]]
sol.updateMatrix(matrix=mat)