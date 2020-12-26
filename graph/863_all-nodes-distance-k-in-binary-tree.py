# 863. All Nodes Distance K in Binary Tree
# Medium
#
# We are given a binary tree (with root node root), a target node, and an integer value K.
# Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.
#
# Example 1:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
# Output: [7,4,1]
#
# Explanation:
# The nodes that are a distance 2 from the target node (with value 5)
# have values 7, 4, and 1.
# Note that the inputs "root" and "target" are actually TreeNodes.
# The descriptions of the inputs above are just serializations of these objects.
#
# Note:
# * The given tree is non-empty.
# * Each node in the tree has unique values 0 <= node.val <= 500.
# * The target node is a node in the tree.
# * 0 <= K <= 1000.

from collections import deque
from typing import List

from helperfunc import TreeNode, build_tree_breadth_first


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        # build graph
        graph = dict()
        self.build_graph(parent=None, child=root, graph=graph)
        distance = 0
        # use bfs to search for distance K apart's nodes
        visited = set()
        visited.add(target)
        q = deque()
        q.append(target)
        rslt = []
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if distance == K:
                    rslt.append(node.val)
                for next_node in graph[node]:
                    if next_node not in visited and next_node is not None:
                        visited.add(next_node)
                        q.append(next_node)
            distance += 1
        return rslt

    def build_graph(self, parent: TreeNode, child: TreeNode, graph):
        for node in [parent, child]:
            if node not in graph:
                graph[node] = set()
        graph[parent].add(child)
        graph[child].add(parent)

        if child.left:
            self.build_graph(child, child.left, graph)
        if child.right:
            self.build_graph(child, child.right, graph)


root = build_tree_breadth_first(sequence=[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])

sol = Solution()
target = root.left
sol.distanceK(root, target, K=2)
