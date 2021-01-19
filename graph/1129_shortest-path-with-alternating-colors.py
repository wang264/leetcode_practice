# 1129. Shortest Path with Alternating Colors
#
# Consider a directed graph, with nodes labelled 0, 1, ..., n-1.  In this graph, each edge is either
# red or blue, and there could be self-edges or parallel edges.
#
#
# Each [i, j] in red_edges denotes a red directed edge from node i to node j.  Similarly, each [i, j] in blue_edges
# denotes a blue directed edge from node i to node j
#
# Return an array answer of length n, where each answer[X] is the length of the shortest path from node 0 to node X such
# that the edge colors alternate along the path (or -1 if such a path doesn't exist).
#
#
# Example 1:
#
# Input: n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
# Output: [0,1,-1]
# Example 2:
#
# Input: n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
# Output: [0,1,-1]
# Example 3:
#
# Input: n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
# Output: [0,-1,-1]
# Example 4:
#
# Input: n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
# Output: [0,1,2]
# Example 5:
#
# Input: n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
# Output: [0,1,1]
#
# Constraints:
#
# 1 <= n <= 100
# red_edges.length <= 400
# blue_edges.length <= 400
# red_edges[i].length == blue_edges[i].length == 2
# 0 <= red_edges[i][j], blue_edges[i][j] < n
#
from typing import List
from collections import deque


class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        red_edges_dic = dict()
        blue_edges_dic = dict()

        for from_node, to_node in red_edges:
            if from_node not in red_edges_dic:
                red_edges_dic[from_node] = set()
            red_edges_dic[from_node].add(to_node)

        for from_node, to_node in blue_edges:
            if from_node not in blue_edges_dic:
                blue_edges_dic[from_node] = set()
            blue_edges_dic[from_node].add(to_node)

        answers = [-1] * n
        q = deque()
        q.append((0, 'red'))  # coming from a red edge , next edge need to be blue
        q.append((0, 'blue'))  # coming from a blue edge, next edge need to be red

        visited_red = set()
        visited_blue = set()
        visited_red.add(0)
        visited_blue.add(0)
        step = 0
        while q:
            for _ in range(len(q)):
                node, color = q.popleft()
                if answers[node] == -1:
                    answers[node] = step
                else:
                    answers[node] = min(answers[node], step)

                if color == 'red' and node in blue_edges_dic.keys():
                    for next_node in blue_edges_dic[node]:
                        if next_node in visited_blue:
                            continue
                        q.append((next_node, 'blue'))
                        visited_blue.add(next_node)

                if color == 'blue' and node in red_edges_dic.keys():
                    for next_node in red_edges_dic[node]:
                        if next_node in visited_red:
                            continue
                        q.append((next_node, 'red'))
                        visited_red.add(next_node)
            step +=1

        return answers


sol = Solution()

sol.shortestAlternatingPaths(n=3, red_edges=[[0, 1]], blue_edges=[[1, 2]])
