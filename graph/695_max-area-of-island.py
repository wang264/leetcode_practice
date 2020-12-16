# 695. Max Area of Island
# Medium
#
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.) You may assume all
#  four edges of the grid are surrounded by water.
# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

# Example 1:
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.

# Example 2:
# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# Note: The length of each dimension in the given grid does not exceed 50.

from collections import deque
from typing import List


class Solution:
    DELTAS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    max_island_size = 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0

        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        max_size = 0
        for row in range(rows):
            for col in range(cols):
                if (row, col) in visited:
                    continue
                if grid[row][col] == 1:
                    visited.add((row,col))
                    self.bfs_walk_island(grid, start_row=row, start_col=col, visited=visited)
                    max_size = max(max_size, self.max_island_size)
                    self.max_island_size = 0

        return max_size

    def bfs_walk_island(self, grid, start_row, start_col, visited):
        q = deque([(start_row, start_col)])
        while q:
            # use bfs
            for _ in range(len(q)):
                land_cell = q.popleft()
                self.max_island_size += 1
                row, col = land_cell
                for d_row, d_col in Solution.DELTAS:
                    next_row = d_row + row
                    next_col = d_col + col

                    if (next_row, next_col) in visited or (not self.is_valid(grid, next_row, next_col)) or \
                            grid[next_row][next_col] != 1:
                        continue
                    q.append((next_row, next_col))
                    visited.add((next_row, next_col))

    def is_valid(self, grid, row, col):
        rows = len(grid)
        cols = len(grid[0])

        return 0 <= row < rows and 0 <= col < cols


sol = Solution()

m = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
     [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]


sol.maxAreaOfIsland(grid=m)
