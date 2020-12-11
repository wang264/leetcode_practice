# 59. Spiral Matrix II
# Medium
#
# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
# Example1:
# Input: n = 3
# Output: [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
#
# Example2:
# Input: n = 1
# Output: [[1]]
#
# Constraints:
# 1 <= n <= 20

from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return []
        rows, cols = n, n
        ans = [[None] * cols for _ in range(rows)]

        drow = [0, 1, 0, -1]
        dcol = [1, 0, -1, 0]

        curr_val = 0
        curr_row = curr_col = state = 0
        for _ in range(rows * cols):
            curr_val += 1
            ans[curr_row][curr_col] = curr_val
            next_row = curr_row + drow[state]
            next_col = curr_col + dcol[state]

            if 0 <= next_row < rows and 0 <= next_col < cols and (ans[next_row][next_col] is None):
                curr_row, curr_col = next_row, next_col
            else:
                state = (state + 1) % 4
                curr_row, curr_col = curr_row + drow[state], curr_col + dcol[state]

        return ans

sol = Solution()
sol.generateMatrix(n=3)