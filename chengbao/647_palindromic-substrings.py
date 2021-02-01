# 647. Palindromic Substrings
# Medium
#
# Share
# Given a string, your task is to count how many palindromic substrings in this string.
#
# The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
#
# Example 1:
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
#
# Example 2:
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
#
# Note:
# The input string length won't exceed 1000.

class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        # aXa, abXba
        for i in range(len(s)):
            ans += self.get_number_of_palindromic_substrings_giving_midpoints(s, i=i, j=i)
        # aXXa, abXXba
        for i in range(len(s) - 1):
            ans += self.get_number_of_palindromic_substrings_giving_midpoints(s, i=i, j=i + 1)
        return ans

    def get_number_of_palindromic_substrings_giving_midpoints(self, s, i: int, j: int):
        count = 0
        n = len(s)
        while i >= 0 and j < n:
            if s[i] == s[j]:
                count += 1
                i -= 1
                j += 1
            else:
                break
        return count


sol = Solution()
sol.countSubstrings(s="fdsklf")