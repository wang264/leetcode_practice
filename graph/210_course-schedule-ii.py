# 210. Course Schedule II
# Medium
#
# There are a total of n courses you have to take labelled from 0 to n - 1.
#
# Some courses may have prerequisites, for example, if prerequisites[i] = [ai, bi] this means you must take the course bi before the course ai.
#
# Given the total number of courses numCourses and a list of the prerequisite pairs, return the ordering of courses you should take to finish all courses.
#
# If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
#
# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
#
# Example 2:
# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
#
# Example 3:
# Input: numCourses = 1, prerequisites = []
# Output: [0]
#
# Constraints:
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= numCourses * (numCourses - 1)
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# ai != bi
# All the pairs [ai, bi] are distinct.

from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        node_to_indegree = {node: 0 for node in range(numCourses)}
        node_to_neighbors = {node: set() for node in range(numCourses)}

        for curr_course, prereq_course in prerequisites:
            node_to_indegree[curr_course] += 1
            node_to_neighbors[prereq_course].add(curr_course)

        q = deque()
        rslt = []
        for node, indegree in node_to_indegree.items():
            if indegree == 0:
                q.append(node)

        while q:
            for _ in range(len(q)):
                curr_node = q.popleft()
                rslt.append(curr_node)
                for neighbor in node_to_neighbors[curr_node]:
                    node_to_indegree[neighbor] -= 1
                    if node_to_indegree[neighbor] == 0:
                        q.append(neighbor)
        if len(rslt) == numCourses:
            return rslt
        else:
            return []
sol = Solution()
sol.findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]])
