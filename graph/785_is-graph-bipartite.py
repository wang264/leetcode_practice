# 785. Is Graph Bipartite?
# Medium
#
# Given an undirected graph, return true if and only if it is bipartite.
#
# Recall that a graph is bipartite if we can split its set of nodes into two independent subsets A and B, such that
# every edge in the graph has one node in A and another node in B.
#
# The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j
# exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges:
# graph[i] does not contain i, and it doesn't contain any element twice.
#
# Example 1:
# Input: graph = [[1,3],[0,2],[1,3],[0,2]]
# Output: true
# Explanation: We can divide the vertices into two groups: {0, 2} and {1, 3}.
#
# Example 2:
# Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
# Output: false
# Explanation: We cannot find a way to divide the set of nodes into two independent subsets.
#
# Constraints:
#
# * 1 <= graph.length <= 100
# * 0 <= graph[i].length < 100
# * 0 <= graph[i][j] <= graph.length - 1
# * graph[i][j] != i
# * All the values of graph[i] are unique.
# * The graph is guaranteed to be undirected.
#
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # status {0:not color, 1:red, -1:blue}
        # color the fist node red and its neighbor blue, then blue's neighbor red.
        # return True if there is conflict
        status = [0 for _ in range(len(graph))]

        # build graph using adjacent list
        g_ = dict()
        for node_1 in range(len(graph)):
            if node_1 not in g_.keys():
                g_[node_1] = set()

            for node_2 in graph[node_1]:

                if node_2 not in g_.keys():
                    g_[node_2] = set()

                g_[node_1].add(node_2)
                g_[node_2].add(node_1)

        for vertex in range(len(graph)):
            if status[vertex] == 0 and not self.dfs_color(vertex, 1, g_, status):
                return False
        return True

    def dfs_color(self, curr_node, color, g_, status) -> bool:
        # return if there is conflict
        status[curr_node] = color
        for next_node in g_[curr_node]:
            # if the neighbor has been color before and it is the same color and current node
            # there is a conflict.
            if status[next_node] == color:
                return False
            # if the neighbor has not been colored, but while color this neighbor we encounter conflick.
            # this mean conflict as well.
            if status[next_node] == 0 and not self.dfs_color(next_node, -1 * color, g_, status):
                return False
        return True


sol = Solution()
sol.isBipartite(graph=[[1,2,3], [0,2], [0,1,3], [0,2]])