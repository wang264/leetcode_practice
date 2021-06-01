# 115. Distinct Subsequences
#
# Given two strings s and t, return the number of distinct subsequences of s which equals t.
#
# A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).
#
# It is guaranteed the answer fits on a 32-bit signed integer.
#
# Example 1:
#
# Input: s = "rabbbit", t = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from S.
# (rabb)b(it)
# (ra)b(bbit)
# (rab)b(bit)
#
# Example 2:
#
# Input: s = "babgbag", t = "bag"
# Output: 5
# Explanation:
# As shown below, there are 5 ways you can generate "bag" from S.
# (ba)b(g)bag
# (ba)bgba(g)
# (b)abgb(ag)
# ba(b)gb(ag)
# babg(bag)

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j] number of distinct subsequence of using first i chars in s and
        # first j letter in t
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

        for i in range(len(s) + 1):
            dp[i][0] = 1  # number of ways using 0 letter in t. 1 way, do not select anything in s.

        for j in range(1, len(t) + 1):  # number of ways using first j letters in s to get first 0 letter in s.
            dp[0][j] = 0

        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[len(s)][len(t)]


sol = Solution()
sol.numDistinct(s="babgbag", t="bag")


