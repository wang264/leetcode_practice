# 827. Making A Large Island
# Hard
#
# In a 2D grid of 0s and 1s, we change at most one 0 to a 1.
#
# After, what is the size of the largest island? (An island is a 4-directionally connected group of 1s).
#
# Example 1:
#
# Input: [[1, 0], [0, 1]]
# Output: 3
# Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
# Example 2:
#
# Input: [[1, 1], [1, 0]]
# Output: 4
# Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
# Example 3:
#
# Input: [[1, 1], [1, 1]]
# Output: 4
# Explanation: Can't change any 0 to 1, only one island with area = 4.
#
# Notes:
# 1 <= grid.length = grid[0].length <= 50.
# 0 <= grid[i][j] <= 1.

from typing import List


class Solution:
    DELTAS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    temp_island_size = 0

    def largestIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        curr_color = 2
        color_to_area = dict()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (not (i, j) in visited):
                    area = self.get_area_and_recursive_flood_fill(grid, curr_color, i, j, visited)
                    color_to_area[curr_color] = area
                    curr_color += 1
        if len(color_to_area) != 0:

            max_area = max(color_to_area.values())
        else:
            max_area = 0
        # iterate all cell that contain zero, and try to use color_to_area to get all the distance.
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 0:
                    continue
                area_if_flip = 1
                islands_can_connect = set()
                for d_row, d_col in self.DELTAS:
                    next_row = d_row + i
                    next_col = d_col + j
                    if self.is_valid(grid, next_row, next_col) and grid[next_row][next_col] != 0:
                        islands_can_connect.add(grid[next_row][next_col])

                for island_color in islands_can_connect:
                    area_if_flip += color_to_area[island_color]
                max_area = max(max_area, area_if_flip)

        return max_area

    def get_area_and_recursive_flood_fill(self, grid, color_to_fill, curr_row, curr_col, visited):
        if not self.is_valid(grid, curr_row, curr_col) or grid[curr_row][curr_col] == 0 or (
                curr_row, curr_col) in visited:
            return 0

        visited.add((curr_row, curr_col))
        grid[curr_row][curr_col] = color_to_fill
        area_sum = 1
        for d_row, d_col in self.DELTAS:
            next_row = d_row + curr_row
            next_col = d_col + curr_col
            area_sum += self.get_area_and_recursive_flood_fill(grid, color_to_fill, next_row, next_col, visited)

        return area_sum

    def is_valid(self, grid, row, col):
        rows = len(grid)
        cols = len(grid[0])

        return 0 <= row < rows and 0 <= col < cols


sol = Solution()
grid = [[0, 1, 0, 1],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 0, 1]]

sol.largestIsland(grid)
