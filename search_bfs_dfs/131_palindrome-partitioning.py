# 131. Palindrome Partitioning
# Medium
#
# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
#
# A palindrome string is a string that reads the same backward as forward.
#
# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
#
# Example 2:
# Input: s = "a"
# Output: [["a"]]
#
# Constraints:
# 1 <= s.length <= 16
# s contains only lowercase English letters.

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        rslt = []
        curr_path = []
        curr_idx = 0
        self.dfs(s, curr_idx, curr_path, rslt)
        return rslt

    def dfs(self, s, curr_idx, curr_path, rslt):
        if curr_idx == len(s):
            rslt.append(curr_path[:])
        for substring_length in range(1, len(s) - curr_idx + 1):
            substring = s[curr_idx:curr_idx + substring_length]
            if not self.is_palindrome(substring):
                continue
            curr_path.append(substring)
            self.dfs(s, curr_idx + substring_length,curr_path,rslt)
            curr_path.pop()

    def is_palindrome(self, s):
        if len(s) == 1:
            return True
        left = 0
        right = len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

sol = Solution()
sol.partition(s="aab")