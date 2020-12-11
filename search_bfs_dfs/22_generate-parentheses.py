# 22. Generate Parentheses
# Medium
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:
# Input: n = 1
# Output: ["()"]
#
# Constraints:
# 1 <= n <= 8

from typing import List


class Solution:
    # +1 for (
    # -1 for )
    # total length is 2n
    # during the process of adding '(' and ')', we can not have a negative number
    def generateParenthesis(self, n: int) -> List[str]:
        curr_path = []
        rslt = []
        curr_count = 0
        self.dfs(n, curr_count, curr_path, rslt)
        return rslt

    def dfs(self, n, curr_count, curr_path, rslt):
        if curr_count < 0 or curr_count > n or len(curr_path)>2*n:
            return
        if len(curr_path) == 2 * n and curr_count == 0:
            rslt.append(''.join(curr_path))
            return
        for char in ['(', ')']:
            if char == '(':
                curr_count += 1
            else:
                curr_count -= 1
            curr_path.append(char)
            self.dfs(n, curr_count, curr_path, rslt)
            curr_path.pop()
            if char == '(':
                curr_count -= 1
            else:
                curr_count += 1


sol = Solution()
sol.generateParenthesis(n=3)
