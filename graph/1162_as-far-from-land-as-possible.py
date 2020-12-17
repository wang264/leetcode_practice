# 1162. As Far from Land as Possible
# Medium
#
# Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find
# a water cell such that its distance to the nearest land cell is maximized, and return the distance.
# If no land or water exists in the grid, return -1.
#
# The distance used in this problem is the Manhattan distance: the distance between two cells
# (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.
#
# Example 1:
# Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
# Output: 2
# Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.
#
# Example 2:
# Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
# Output: 4
# Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.
#
# Constraints:
# * n == grid.length
# * n == grid[i].length
# * 1 <= n <= 100
# * grid[i][j] is 0 or 1

from collections import deque
from typing import List


class Solution:
    # memorization search.
    DELTAS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def maxDistance(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        distance = [[None] * cols for _ in range(rows)]
        visited = [[False] * cols for _ in range(rows)]
        q = deque()
        curr_step = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    visited[i][j] = True
                    q.append((i, j))
        # if no land exist or no water exist:
        if len(q) == 0 or len(q)==rows*cols:
            return -1
        while q:
            for _ in range(len(q)):
                curr_row, curr_col = q.popleft()
                distance[curr_row][curr_col] = curr_step
                for d_row, d_col in self.DELTAS:
                    next_row, next_col = d_row + curr_row, d_col + curr_col
                    # we visit it before
                    if not self.is_valid(grid, next_row, next_col) or visited[next_row][next_col]:
                        continue
                    visited[next_row][next_col] = True
                    q.append((next_row, next_col))

            curr_step += 1

        max_distance = 0
        for i in range(rows):
            for j in range(cols):
                max_distance = max(max_distance, distance[i][j])
        return max_distance

    def is_valid(self, grid, row, col):
        rows = len(grid)
        cols = len(grid[0])

        return 0 <= row < rows and 0 <= col < cols


sol = Solution()
sol.maxDistance(grid=[[1, 0], [0, 0]])
