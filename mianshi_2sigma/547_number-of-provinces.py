# 547. Number of Provinces
# Medium

# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b,
# and city b is connected directly with city c, then city a is connected indirectly with city c.
#
# A province is a group of directly or indirectly connected cities and no other cities outside of the group.
#
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are
# directly connected, and isConnected[i][j] = 0 otherwise.
#
# Return the total number of provinces.

# Example 1:
# Input: isConnected = [[1,1,0],
#                       [1,1,0],
#                       [0,0,1]]
# Output: 2

# Example 2:
# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3

# Constraints:
# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] is 1 or 0.
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]

from typing import List


class Solution:
    def __init__(self):
        self.father = {}
        self.num_connected = None

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        self.num_connected = n
        self.father = {x: x for x in range(0, n)}
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    self.union(i, j)

        return self.num_connected

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            self.father[root_a] = root_b
            self.num_connected -= 1

    def find(self, x):
        # if x is its own father
        if self.father[x] == x:
            return x

        # find root
        root = x
        while self.father[root] != root:
            root = self.father[root]

        # path compression
        while self.father[x] != root:
            temp = self.father[x]
            self.father[x] = root
            x = temp

        return root


sol = Solution()
sol.findCircleNum(isConnected=[[1, 1, 1], [1, 1, 1], [1, 1, 1]])
