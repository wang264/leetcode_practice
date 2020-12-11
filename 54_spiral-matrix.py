# 54. Spiral Matrix
# Medium
#
# Given an m x n matrix, return all elements of the matrix in spiral order.
#
# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
#
# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#
# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100
#
#
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        rows, cols = len(matrix), len(matrix[0])
        visited = [[False] * cols for _ in range(rows)]

        ans = []
        drow = [0, 1, 0, -1]
        dcol = [1, 0, -1, 0]

        curr_row = curr_col = state = 0
        for _ in range(rows * cols):
            ans.append(matrix[curr_row][curr_col])
            visited[curr_row][curr_col] = True
            next_row = curr_row + drow[state]
            next_col = curr_col + dcol[state]

            if 0 <= next_row < rows and 0 <= next_col < cols and (not visited[next_row][next_col]):
                curr_row, curr_col = next_row, next_col
            else:
                state = (state + 1) % 4
                curr_row, curr_col = curr_row + drow[state], curr_col + dcol[state]

        return ans


sol = Solution()
sol.spiralOrder(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
