# 675. Cut Off Trees for Golf Event
# Hard
#
# You are asked to cut off all the trees in a forest for a golf event. The forest is represented as an m x n matrix. In this matrix:
# 0 means the cell cannot be walked through.
# 1 represents an empty cell that can be walked through.
# A number greater than 1 represents a tree in a cell that can be walked through, and this number is the tree's height.
# In one step, you can walk in any of the four directions: north, east, south, and west. If you are standing in a cell with a tree, you can choose whether to cut it off.
# You must cut off the trees in order from shortest to tallest. When you cut off a tree, the value at its cell becomes 1 (an empty cell).
# Starting from the point (0, 0), return the minimum steps you need to walk to cut off all the trees. If you cannot cut off all the trees, return -1.
# You are guaranteed that no two trees have the same height, and there is at least one tree needs to be cut off.

# Example 1:
# Input: forest = [[1,2,3],[0,0,4],[7,6,5]]
# Output: 6
# Explanation: Following the path above allows you to cut off the trees from shortest to tallest in 6 steps.
#
# Example 2:
# Input: forest = [[1,2,3],[0,0,0],[7,6,5]]
# Output: -1
# Explanation: The trees in the bottom row cannot be accessed as the middle row is blocked.
#
# Example 3:
# Input: forest = [[2,3,4],[0,0,5],[8,7,6]]
# Output: 6
# Explanation: You can follow the same path as Example 1 to cut off all the trees.
# Note that you can cut off the first tree at (0, 0) before making any steps.


# Constraints:
# m == forest.length
# n == forest[i].length
# 1 <= m, n <= 50
# 0 <= forest[i][j] <= 109

import collections


class Solution(object):
    def cutOffTree(self, forest):
        trees = sorted((value, r, c) for r, row in enumerate(forest)
                       for c, value in enumerate(row) if value > 1)

        start_row = start_col = ans = 0
        for _, target_row, target_col in trees:
            distance = self.dist_bfs(forest, start_row, start_col, target_row, target_col)
            if distance < 0:
                return -1
            ans += distance
            start_row, start_col = target_row, target_col
        return ans

    def dist_bfs(self, forest, sr, sc, tr, tc):
        R, C = len(forest), len(forest[0])
        queue = collections.deque([(sr, sc, 0)])
        seen = {(sr, sc)}
        while queue:
            r, c, d = queue.popleft()
            if r == tr and c == tc:
                return d
            for next_row, next_col in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if (0 <= next_row < R and 0 <= next_col < C and
                        (next_row, next_col) not in seen and forest[next_row][next_col]):
                    seen.add((next_row, next_col))
                    queue.append((next_row, next_col, d + 1))
        return -1
