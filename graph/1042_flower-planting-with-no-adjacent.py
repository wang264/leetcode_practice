# 1042. Flower Planting With No Adjacent
# Medium
#
# You have n gardens, labeled from 1 to n, and an array paths where paths[i] = [xi, yi] describes a bidirectional path between garden xi to garden yi. In each garden, you want to plant one of 4 types of flowers.
#
# All gardens have at most 3 paths coming into or leaving it.
#
# Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.
#
# Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)th garden. The flower types are denoted 1, 2, 3, or 4. It is guaranteed an answer exists.
#
# Example 1:
# Input: n = 3, paths = [[1,2],[2,3],[3,1]]
# Output: [1,2,3]
# Explanation:
# Gardens 1 and 2 have different types.
# Gardens 2 and 3 have different types.
# Gardens 3 and 1 have different types.
# Hence, [1,2,3] is a valid answer. Other valid answers include [1,2,4], [1,4,2], and [3,2,1].
#
# Example 2:
# Input: n = 4, paths = [[1,2],[3,4]]
# Output: [1,2,1,2]
#
# Example 3:
# Input: n = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
# Output: [1,2,3,4]
#
# Constraints:
# * 1 <= n <= 104
# * 0 <= paths.length <= 2 * 104
# * paths[i].length == 2
# * 1 <= xi, yi <= n
# * xi != yi
# * Every garden has at most 3 paths coming into or leaving it.

from typing import List


#
# 这个题目背景虽然是花园，但是我相信大家应该都明白了，其实说的是四色定理。
# 既然是个图论的题目，那么就按照图的方法来解。先构建无向图，对于每个顶点检查其所有相邻顶点的编号，
# 这个顶点用一个没有用过的编号，依次类推。题目也已经说了，解一定存在。
# 由于每个顶点最多只有三条边，所以时间复杂度是O(N)。
# Python代码如下：
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        rslt = [0] * (n + 1)

        graph = {node: set() for node in range(1, n + 1)}
        for node_a, node_b in paths:
            graph[node_a].add(node_b)
            graph[node_b].add(node_a)

        for node in range(1, n + 1):
            neighbor_colors = set()
            # get all neighbor's color
            for neighbor in graph[node]:
                neighbor_colors.add(rslt[neighbor])
            # iterate possible neighbor colors
            for possible_color in range(1, 5):
                if possible_color in neighbor_colors:
                    continue
                rslt[node] = possible_color
                break

        # answer must exist
        return rslt[1:]
