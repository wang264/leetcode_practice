# 40. Combination Sum II
# Medium
#
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.
#
# Example 1:
#
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
#
# Example 2:
# Input: candidates = [2,5,2,1,2], target = 5
# Output:
# [
# [1,2,2],
# [5]
# ]
#
# Constraints:
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30

from typing import List


class Solution:

    # we need to sort first,
    # to prevent duplication, for example, 1,1',1'',2,2',3,4
    # 1 need to be selected first before we can select 1'
    # and 1 and 1' need to be selected before we can select 1'''

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        curr_path = []
        curr_sum = 0
        rslt = []
        curr_index = 0
        selected = [False for _ in range(len(candidates))]

        self.dfs(candidates, curr_index, curr_sum, curr_path, target, rslt, selected)
        return rslt

    def dfs(self, candidates, curr_index, curr_sum, curr_path, target, rslt, selected):
        if curr_sum == target:
            rslt.append(curr_path[:])
            return
        if curr_sum > target:
            return

        for i in range(curr_index, len(candidates)):
            # this number and the previous number is the same and you have not selected the previous one
            if i > 0 and candidates[i - 1] == candidates[i] and (not selected[i - 1]):
                continue
            selected[i] = True
            curr_path.append(candidates[i])
            curr_sum += candidates[i]
            self.dfs(candidates, i + 1, curr_sum, curr_path, target, rslt, selected)
            curr_sum -= candidates[i]
            curr_path.pop()
            selected[i] = False


sol = Solution()
sol.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8)
