# 952. Largest Component Size by Common Factor
# Hard
#
# Given a non-empty array of unique positive integers A, consider the following graph:
# * There are A.length nodes, labelled A[0] to A[A.length - 1];
# * There is an edge between A[i] and A[j] if and only if A[i] and A[j] share a common factor greater than 1.
#
# Return the size of the largest connected component in the graph.

# Example 1:
# Input: [4,6,15,35]
# Output: 4
#
# Example 2:
# Input: [20,50,9,63]
# Output: 2
#
# Example 3:
# Input: [2,3,6,7,4,12,21,39]
# Output: 8
#
# Note:
# 1 <= A.length <= 20000
# 1 <= A[i] <= 100000

import math
from typing import List
import collections

class Solution:
    def __init__(self):
        self.father = dict()
        self.root_to_block_size = dict()

    def largestComponentSize(self, A: List[int]) -> int:
        # for each number, union itself with all its factors
        for a in A:
            if a not in self.father.keys():
                self.father[a] = a
                self.root_to_block_size[a] = 1

            for k in range(2, int(math.sqrt(a) + 1)):
                if a % k == 0:
                    for key in [k, a // k]:
                        if key not in self.father.keys():
                            self.father[key] = key
                            self.root_to_block_size[key] = 1

                    self.union(a, k)
                    self.union(a, a // k)
        # find the largest component.
        return collections.Counter([self.find(a) for a in A]).most_common(1)[0][1]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.root_to_block_size[root_a] += self.root_to_block_size[root_b]
            del self.root_to_block_size[root_b]
            self.father[root_b] = root_a

    def find(self, x):
        # if x is root
        if self.father[x] == x:
            return x
        # find root
        root = x
        while self.father[root] != root:
            root = self.father[root]

        # path compression
        while self.father[x] != root:
            temp = self.father[x]
            self.father[x] = root
            x = temp

        return root


sol = Solution()
sol.largestComponentSize(A=[20, 50, 9, 63])
