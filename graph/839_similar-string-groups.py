# 839. Similar String Groups
# Hard
#
# Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y. Also two strings X and Y are similar if they are equal.
#
# For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".
#
# Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.
#
# We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?
#
# Example 1:
# Input: strs = ["tars","rats","arts","star"]
# Output: 2
#
# Example 2:
# Input: strs = ["omv","ovm"]
# Output: 1
#
# Constraints:
# * 1 <= strs.length <= 100
# * 1 <= strs[i].length <= 1000
# * sum(strs[i].length) <= 2 * 104
# * strs[i] consists of lowercase letters only.
# * All words in strs have the same length and are anagrams of each other.
from typing import List


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                if self.is_similar(strs[i], strs[j]):
                    self.union(strs[i], strs[j])
        roots = set()
        for x in strs:
            roots.add(self.find(x))
        return len(roots)

    def is_similar(self, str_a, str_b):
        if len(str_a) != len(str_b):
            return False
        num_diff = 0
        for i in range(len(str_a)):
            if str_a[i] != str_b[i]:
                num_diff += 1
            if num_diff > 2:
                return False
        if num_diff == 0 or num_diff == 2:
            return True
        else:
            return False

    def __init__(self):
        self.father = dict()

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_b] = root_a

    def find(self, x):
        if x not in self.father.keys():
            self.father[x] = x
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
sol.numSimilarGroups( strs = ["tars","rats","arts","star"])