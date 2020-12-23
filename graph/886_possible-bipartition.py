# 886. Possible Bipartition
# Medium
#
# Share
# Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.
#
# Each person may dislike some other people, and they should not go into the same group.
#
# Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.
#
# Return true if and only if it is possible to split everyone into two groups in this way.
#
# Example 1:
# Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: group1 [1,4], group2 [2,3]
#
# Example 2:
# Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
# Output: false
#
# Example 3:
# Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# Output: false
#
# Constraints:
# * 1 <= N <= 2000
# * 0 <= dislikes.length <= 10000
# * dislikes[i].length == 2
# * 1 <= dislikes[i][j] <= N
# * dislikes[i][0] < dislikes[i][1]
# * There does not exist i != j for which dislikes[i] == dislikes[j].

from typing import List


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        # status {0:not color, 1:red, -1:blue}
        # color the fist node red and its neighbor blue, then blue's neighbor red.
        # return True if there is conflict
        status = [0 for _ in range(0, N+1)]
        # build graph using adjacent list
        g_ = dict()
        for node in range(1, N+1):
            g_[node] = set()
        for node_1, node_2 in dislikes:
            g_[node_1].add(node_2)
            g_[node_2].add(node_1)

        for vertex in range(1, N+1):
            if status[vertex] == 0 and not self.dfs_color(vertex, 1, g_, status):
                return False
        return True

    def dfs_color(self, curr_node, color, g_, status):
        status[curr_node] = color

        for next_node in g_[curr_node]:
            # if next node has color and it is conflict
            if status[next_node] != 0 and status[next_node] == color:
                return False
            # if next node do NOT have color yet, but have conflict coloring it
            if status[next_node] == 0 and not self.dfs_color(next_node, -1 * color, g_, status):
                return False
        return True

#
# sol = Solution()
# sol.possibleBipartition(N=4, dislikes=[[1, 3], [0, 2], [1, 3], [0, 2]])

sol = Solution()
sol.possibleBipartition(N=4, dislikes=[[1, 2], [1, 3], [2, 4]])
