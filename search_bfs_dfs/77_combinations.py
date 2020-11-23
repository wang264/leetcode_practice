# 77. Combinations
# Medium
#
# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
# You may return the answer in any order.
#
# Example 1:
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
#
# Example 2:
# Input: n = 1, k = 1
# Output: [[1]]
#
# Constraints:
# 1 <= n <= 20
# 1 <= k <= n

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        curr_path = []
        rslt = []
        curr_number = 1
        self.dfs(n, curr_number, curr_path, k, rslt)
        return rslt

    def dfs(self, max_number, curr_number, curr_path, k, rslt):
        if len(curr_path) == k:
            rslt.append(curr_path[:])

        # from curr_number to max_number
        for num in range(curr_number, max_number + 1):
            curr_path.append(num)
            self.dfs(max_number, num + 1, curr_path, k, rslt)
            curr_path.pop()


sol = Solution()
sol.combine(n=4, k=2)
