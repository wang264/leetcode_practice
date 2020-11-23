# 216. Combination Sum III
# Medium

# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
#
# Only numbers 1 through 9 are used.
# Each number is used at most once.
# Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

# Example 1:
#
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Explanation:
# 1 + 2 + 4 = 7
# There are no other valid combinations.
# Example 2:
#
# Input: k = 3, n = 9
# Output: [[1,2,6],[1,3,5],[2,3,4]]
# Explanation:
# 1 + 2 + 6 = 9
# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# There are no other valid combinations.
# Example 3:
#
# Input: k = 4, n = 1
# Output: []
# Explanation: There are no valid combinations. [1,2,1] is not valid because 1 is used twice.
# Example 4:
#
# Input: k = 3, n = 2
# Output: []
# Explanation: There are no valid combinations.
# Example 5:
#
# Input: k = 9, n = 45
# Output: [[1,2,3,4,5,6,7,8,9]]
# Explanation:
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
# ​​​​​​​There are no other valid combinations.
#
# Constraints:
#
# 2 <= k <= 9
# 1 <= n <= 60

from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        curr_path = []
        curr_num = 1  # from 1---9 because only number from 1---9 can be used.
        rslt = []
        curr_sum = 0
        self.dfs(k, n, curr_sum, curr_num, curr_path, rslt)
        return rslt

    def dfs(self, k, n, curr_sum, curr_num, curr_path, rslt):
        if curr_sum == n and len(curr_path) == k:
            rslt.append(curr_path[:])
            return
        if len(curr_path) > k:
            return
        if curr_sum > n:
            return
        if curr_num > 9:
            return
        # from curr_num to 9.
        for num in range(curr_num, 10):
            curr_path.append(num)
            curr_sum += num
            self.dfs(k, n, curr_sum, num + 1, curr_path, rslt)
            curr_sum -=num
            curr_path.pop()


sol = Solution()
sol.combinationSum3(k=3, n=9)
