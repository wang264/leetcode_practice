# 784. Letter Case Permutation
# Medium
#
# Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.
# Return a list of all possible strings we could create. You can return the output in any order.
#
# Example 1:
# Input: S = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]
#
# Example 2:
# Input: S = "3z4"
# Output: ["3z4","3Z4"]
#
# Example 3:
# Input: S = "12345"
# Output: ["12345"]
#
# Example 4:
# Input: S = "0"
# Output: ["0"]
#
# Constraints:
# S will be a string with length between 1 and 12.
# S will consist only of letters or digits.

from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        curr_idx = 0
        curr_path = []
        rslt = []
        self.dfs(S, curr_idx, curr_path, rslt)
        return rslt

    def dfs(self, S, curr_idx, curr_path, rslt):
        if len(curr_path) == len(S):
            rslt.append(''.join(curr_path))
            return

        if not S[curr_idx].isalpha():
            curr_path.append(S[curr_idx])
            self.dfs(S, curr_idx + 1, curr_path, rslt)
            curr_path.pop()
        else:
            for char in [S[curr_idx].lower(), S[curr_idx].upper()]:
                curr_path.append(char)
                self.dfs(S, curr_idx + 1, curr_path, rslt)
                curr_path.pop()


sol = Solution()
sol.letterCasePermutation(S="a1b2")
