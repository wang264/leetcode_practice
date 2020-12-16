# 733. Flood Fill
# An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).
#
# Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.
#
# To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.
#
# At the end, return the modified image.
#
# Example 1:
# Input:
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation:
# From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
# by a path of the same color as the starting pixel are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected
# to the starting pixel.

# Note:
# The length of image and image[0] will be in the range [1, 50].
# The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
# The value of each color in image[i][j] and newColor will be an integer in [0, 65535].

from collections import deque
from typing import List


class Solution:
    DELTAS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        old_color = image[sr][sc]
        new_color = newColor

        visited = set()
        visited.add((sr, sc))
        q = deque([(sr, sc)])

        while q:
            for _ in range(len(q)):
                curr_row, curr_col = q.popleft()
                image[curr_row][curr_col] = new_color
                for d_row, d_col in self.DELTAS:
                    next_row = d_row + curr_row
                    next_col = d_col + curr_col
                    if self.is_valid(image, next_row, next_col) and ((next_row, next_col) not in visited) and \
                            image[next_row][next_col] == old_color:
                        visited.add((next_row, next_col))
                        q.append((next_row, next_col))
        return image

    def is_valid(self, grid, row, col):
        rows = len(grid)
        cols = len(grid[0])

        return 0 <= row < rows and 0 <= col < cols


sol = Solution()
image = [[1, 1, 1],
         [1, 1, 0],
         [1, 0, 1]]
sr = 1
sc = 1
newColor = 2
sol.floodFill(image, sr, sc, 2)
