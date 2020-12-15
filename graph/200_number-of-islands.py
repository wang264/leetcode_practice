# 200. Number of Islands
# Medium
#
# Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.
#
#
# Example 1:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
#
# Example 2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#
# Constraints:
# * m == grid.length
# * n == grid[i].length
# * 1 <= m, n <= 300
# * grid[i][j] is '0' or '1'.

from collections import deque
from typing import List


class Solution:
    DELTAS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        visited = set()
        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if (row, col) in visited:
                    continue
                if grid[row][col] == '1':
                    islands += 1
                    self.bfs_walk_island(grid, start_row=row, start_col=col, visited=visited)

        return islands

    def bfs_walk_island(self, grid, start_row, start_col, visited):
        q = deque([(start_row, start_col)])
        while q:
            # use bfs
            for _ in range(len(q)):
                land_cell = q.popleft()
                row, col = land_cell
                for d_row, d_col in Solution.DELTAS:
                    next_row = d_row + row
                    next_col = d_col + col

                    if (next_row, next_col) in visited or (not self.is_valid(grid, next_row, next_col)) or grid[next_row][next_col] != '1':
                        continue
                    q.append((next_row, next_col))
                    visited.add((next_row, next_col))

    def is_valid(self, grid, row, col):
        rows = len(grid)
        cols = len(grid[0])

        return 0 <= row < rows and 0 <= col < cols

sol = Solution()
matrix = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

sol.numIslands(grid=matrix)