# 207. Course Schedule
# Medium
#
#
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all course
#
# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
#              To take course 1 you should have finished course 0. So it is possible.
# Example 2:
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.
#
# Constraints:
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# 1 <= numCourses <= 10^5

from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        directed_edges = {node: set() for node in range(numCourses)}
        node_to_indegree = {node: 0 for node in range(numCourses)}

        for curr_course, prereq_course in prerequisites:
            directed_edges[prereq_course].add(curr_course)
            node_to_indegree[curr_course] += 1
        visited = set()
        q = deque()
        for node in node_to_indegree.keys():
            if node_to_indegree[node] == 0:
                q.append(node)
                visited.add(node)

        if len(q) == 0:
            return False

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for neighbor in directed_edges[node]:
                    node_to_indegree[neighbor] -= 1
                    if node_to_indegree[neighbor] == 0:
                        visited.add(neighbor)
                        q.append(neighbor)

        return len(visited) == numCourses


sol = Solution()
sol.canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]])
