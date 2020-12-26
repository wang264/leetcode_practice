# 433. Minimum Genetic Mutation
# Medium
#
# A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".
#
# Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.
#
# For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.
#
# Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.
#
# Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.
#
# Note:
# * Starting point is assumed to be valid, so it might not be included in the bank.
# * If multiple mutations are needed, all mutations during in the sequence must be valid.
# * You may assume start and end string is not the same.
#
# Example 1:
# start: "AACCGGTT"
# end:   "AACCGGTA"
# bank: ["AACCGGTA"]
# return: 1
#
# Example 2:
# start: "AACCGGTT"
# end:   "AAACGGTA"
# bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
# return: 2
#
# Example 3:
# start: "AAAAACCC"
# end:   "AACCCCCC"
# bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
# return: 3

from collections import deque
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # solve using bfs
        visited = set()
        q = deque()
        q.append(start)
        visited.add(start)
        step = 0
        while q:
            for _ in range(len(q)):
                curr_gene = q.popleft()
                if curr_gene == end:
                    return step
                for next_gene in self.get_valid_mutates(start=curr_gene, bank=bank):
                    if next_gene not in visited:
                        q.append(next_gene)
                        visited.add(next_gene)

            step += 1

        return -1

    def get_valid_mutates(self, start: str, bank: List[str]):
        n = len(start)
        valid_mutates = []
        for i in range(n):
            for gene in ["A", "C", "G", "T"]:
                new_gene = start[0:i] + gene + start[i + 1:]
                if new_gene in bank:
                    valid_mutates.append(new_gene)
        return valid_mutates


sol = Solution()
start = "AAAAACCC"
end = "AACCCCCC"
bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
sol.minMutation(start,end,bank)
