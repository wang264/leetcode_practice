# Please code in Python or Java or C++, If you know how to do N-Root or N-queens problem in relation to this problem,
# that is even better.
#
# A retail store chain wants to expand into a new neighborhood. To maximize the number of clients, the new branch
# should be at a distance of no more than K distance from all the houses in the neighborhood.
# A is a matrix of size N x M, representing the neighborhood as a rectangular grid, in which each cell is either
# an integer 0 (an empty pick) or 1 (a house). The distance between two cells is calculated as the minimum number of
# cell borders (regardless of whether the cells on the way are empty or occupied) that one has to cross to move from
# the source to the target cell (without moving through corners). A store can be only built on an empty plot.
# How many suitable locations are there?
#
# For example, given K = 2 and matrix A = [ [0,0,0,0][0,0,1,0][1,0,0,1]] houses are located in cells with coordinates
# (2,3), (3,1) and (3,4). We can build a new store on two empty plots that are close enough to all the houses.
# The first possible empty plot is located at (3,2). The distance to the first house at (2,3) is 2, the distance
# to the second house at (3,1) is 1, and the third house at (3,4) is at a distance of 2. The second possible empty
# plot is located at (3,3). The distance to the first, second and third house are respectively 1, 2 and 1.
#
# Write a function: def solution(K, A):
#
# Where K is a positive integer and matrix A size of N x M, function returns the number of empty plots that
# are close enough to all the houses.
#
# EXAMPLES:
#
# 1. Given K = 2, and A = [[0,0,0,0],[0,0,1,0],[1,0,0,1]], the function should return 2, as explained above.
#
# 2. Given K = 1 and A = [[0,1], [0,0]], the function should return 2. We can build a store on empty
# plots at (1,1) and (2,2).


import sys
from collections import deque

HOUSE = 1
LAND = 0
DELTAS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class Solution:
    def possible_locations(self, A, K):
        rows = len(A)
        cols = len(A[0])

        houses = []
        for i in range(rows):
            for j in range(cols):
                if A[i][j] == HOUSE:
                    houses.append((i, j))

        max_dist = [[-1 * sys.maxsize] * cols for _ in range(rows)]
        for cord in houses:
            self.bfs_helper(A, cord, max_dist)

        count = 0
        for i in range(rows):
            for j in range(cols):
                if A[i][j] == LAND and max_dist[i][j] <= K:
                    count += 1
        return count

    def bfs_helper(self, A, cord, max_dist):
        q = deque([])
        visited = set()
        visited.add(cord)
        q.append(cord)

        curr_dist = 0
        while q:
            for _ in range(len(q)):
                curr_cord = q.popleft()
                curr_x, curr_y = curr_cord
                max_dist[curr_x][curr_y] = max(max_dist[curr_x][curr_y], curr_dist)

                for d_x, d_y in DELTAS:
                    next_x = curr_x + d_x
                    next_y = curr_y + d_y
                    if self.is_valid_location(A, next_x, next_y) and ((next_x, next_y) not in visited):
                        q.append((next_x, next_y))
                        visited.add((next_x, next_y))

            curr_dist += 1

    def is_valid_location(self, A, x, y):
        rows = len(A)
        cols = len(A[0])
        return 0 <= x < rows and 0 <= y < cols


sol = Solution()
sol.possible_locations(A=[[0, 0, 0, 0], [0, 0, 1, 0], [1, 0, 0, 1]], K=2)

sol.possible_locations(A=[[0, 1], [0, 0]], K=1)
