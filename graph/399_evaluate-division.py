# # 399. Evaluate Division
# # Medium
# #
# # You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
# #
# # You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
# #
# # Return the answers to all queries. If a single answer cannot be determined, return -1.0.
# #
# # Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.
#
# Example 1:
# Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation:
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
#
# Example 2:
# Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# Output: [3.75000,0.40000,5.00000,0.20000]
#
# Example 3:
# Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
# Output: [0.50000,2.00000,-1.00000,-1.00000]
#
# Constraints:
# * 1 <= equations.length <= 20
# * equations[i].length == 2
# * 1 <= Ai.length, Bi.length <= 5
# * values.length == equations.length
# * 0.0 < values[i] <= 20.0
# * 1 <= queries.length <= 20
# * queries[i].length == 2
# * 1 <= Cj.length, Dj.length <= 5
# * Ai, Bi, Cj, Dj consist of lower case English letters and digits.

from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = dict()
        # g[A][B] = k -> A / B = k
        for equation, value in zip(equations, values):
            a = equation[0]
            b = equation[1]
            k = value
            if a not in graph.keys():
                graph[a] = dict()
            if b not in graph.keys():
                graph[b] = dict()
            graph[a][b] = k
            graph[b][a] = 1 / k

        rslt = []
        for query in queries:
            visited = set()
            rslt.append(self.dfs_find_rslt(query[0], query[1], graph, visited))
        return rslt

    def dfs_find_rslt(self, A, B, graph: dict, visited: set):
        if A not in graph or B not in graph:
            return -1
        if A == B:
            return 1
        visited.add(A)
        # A/B = A/C*C/B
        for C in graph[A].keys():
            if C in visited:
                continue
            d = self.dfs_find_rslt(C, B, graph, visited)
            if d > 0:
                return graph[A][C] * d
        return -1


sol = Solution()
equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

sol.calcEquation(equations, values, queries)
