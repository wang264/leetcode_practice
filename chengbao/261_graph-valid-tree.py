# Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes),
# write a function to check whether these edges make up a valid tree.

# Example 1:
# Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
# Output: true
# Example 2:
# Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# Output: false


# Before solving the problem, we have to know the definitions.
# Tree vs Graph
# A tree is a special undirected graph. It satisfy two properties
# 1.It is connected
# 2.It has no cycle.

# Being connected means you can start from any node and reach any other node. To prove it, we can do
# a DFS and add each node we visit to a set. After we visited all the nodes, we compare the number
# of nodes in the set with the total number of nodes. If they are the same then every node is
# accessible from any other node and the graph is connected.
# To prove an undirected graph having no cycle, we can also do a DFS. If a graph contains a cycle,
# then we would visit a certain node more than once. There is a minor caveat, since the graph
# is undirected, when we visit a child we would always add parent to the next visit list.
# This creates a trivial cycle and not the real cycle we want. We can avoid detecting trivial
# cycle but adding an additional parent state in the DFS call.
# We can check both properties in one DFS call since cycle detection always keeps track
# of a visited set.

from collections import defaultdict
from collections import deque


class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def validTree(self, n, edges):
        # build graph

        graph = {i: set() for i in range(n)}
        for from_edge, to_edge in edges:
            graph[from_edge].add(to_edge)
            graph[to_edge].add(from_edge)

        q = deque([(0, -1)])
        visited = set()
        visited.add((0, -1))

        while q:
            for _ in range(len(q)):
                node, from_node = q.popleft()
                for next_node in graph[node]:
                    if next_node == from_node:
                        continue
                    if next_node in visited:
                        return False
                    visited.add((next_node, node))
                    q.append((next_node, node))

        if len(visited) == n:
            return True
        else:
            return False


sol = Solution()
sol.validTree(n=5, edges=[[0, 1], [0, 2], [0, 3], [1, 4]])

from collections import deque


class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    # valid if it connect to one component
    # valid if it len(edges)==n-1

    # we use union find algorithm
    def __init__(self):
        self.father = dict()
        self.components = None

    def validTree(self, n, edges):
        # init
        for i in range(n):
            self.father[i] = i
        self.components = n

        for from_edge, to_edge in edges:
            self.union(from_edge, to_edge)

        return len(edges) == n - 1 and self.components == 1

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            self.father[root_b] = root_a
            self.components -= 1

    def find(self, x):
        # if x is root
        if self.father[x] == x:
            return x
        # try to find root
        root = x
        while self.father[root] != root:
            root = self.father[root]

        # path compression
        while self.father[x] != root:
            temp = self.father[x]
            self.father[x] = root
            x = temp

        return root

