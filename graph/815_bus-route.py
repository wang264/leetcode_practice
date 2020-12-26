# 815. Bus Routes
# Hard
# We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever. For example
# if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.
#
# We start at bus stop S (initially not on a bus), and we want to go to bus stop T. Travelling by buses
# only, what is the least number of buses we must take to reach our destination? Return -1 if it is not possible.
#
# Example:
# Input:
# routes = [[1, 2, 7], [3, 6, 7]]
# S = 1
# T = 6
# Output: 2
# Explanation:
# The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
#
# Constraints:
# * 1 <= routes.length <= 500.
# * 1 <= routes[i].length <= 10^5.
# * 0 <= routes[i][j] < 10 ^ 6.

from collections import deque
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        # use bfs to solve this problem
        # build graph
        graph = dict()
        for route in routes:
            for i in range(len(route) - 1):
                if route[i] not in graph.keys():
                    graph[route[i]] = set()
                for j in range(i + 1, len(route)):
                    if route[j] not in graph.keys():
                        graph[route[j]] = set()
                    graph[route[i]].add(route[j])
                    graph[route[j]].add(route[i])

        visited = set()
        visited.add(S)
        q = deque()
        q.append(S)
        num_step = 0

        while q:
            for _ in range(len(q)):
                curr_stop = q.popleft()
                if curr_stop == T:
                    return num_step
                for next_stop in graph[curr_stop]:
                    if next_stop not in visited:
                        q.append(next_stop)
                        visited.add(next_stop)

            num_step += 1

        return -1


sol = Solution()
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
sol.numBusesToDestination(routes, S, T)

routes = [[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]]
S = 15
T = 12
sol.numBusesToDestination(routes, S, T)
