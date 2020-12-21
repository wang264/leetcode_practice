# 990. Satisfiability of Equality Equations
# Medium
#
# Given an array equations of strings that represent relationships between variables, each string equations[i] has
# length 4 and takes one of two different forms: "a==b" or "a!=b".  Here, a and b are lowercase letters
# (not necessarily different) that represent one-letter variable names.
#
# Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.
#
# Example 1:
# Input: ["a==b","b!=a"]
# Output: false
# Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
# There is no way to assign the variables to satisfy both equations.
#
# Example 2:
# Input: ["b==a","a==b"]
# Output: true
# Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
#
# Example 3:
# Input: ["a==b","b==c","a==c"]
# Output: true
#
# Example 4:
# Input: ["a==b","b!=c","c==a"]
# Output: false
#
# Example 5:
# Input: ["c==c","b==d","x!=z"]
# Output: true
#
# Note:
# * 1 <= equations.length <= 500
# * equations[i].length == 4
# * equations[i][0] and equations[i][3] are lowercase letters
# * equations[i][1] is either '=' or '!'
# * equations[i][2] is '='

from typing import List


class Solution:

    def __init__(self):
        self.father = dict()

    def equationsPossible(self, equations: List[str]) -> bool:
        # b/c equations[i].length == 4
        for equation in equations:
            left, operation, right = equation[0], equation[1:3], equation[3]
            # init
            for key in [left, right]:
                if key not in self.father:
                    self.father[key] = key
            if operation == "==":
                self.union(a=left, b=right)

        for equation in equations:
            left, operation, right = equation[0], equation[1:3], equation[3]
            if operation == "!=":
                if self.is_connected(a=left, b=right):
                    return False
        return True

    def union(self, a, b):

        root_a = self.find(a)
        root_b = self.find(b)

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

    def is_connected(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return True
        else:
            False


sol = Solution()
sol.equationsPossible(equations=["a==b", "b!=c", "c==a"])