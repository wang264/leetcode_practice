# We are given a string S consisting of N lowercase letters.
# A sequence of two adjacent letters inside a string is called a digram. The distance between two digrams is
# the distance between the first letter of the first digram and the first letter of the second digram.
# For example, in string S = "abcde" the distance between digrams "bc" and "de" is 2. We want to find the
# distance between the furthest identical digrams inside string S. Write a function: that, given a string S
# consisting of N letters, returns the distance between the two identical digrams in the string that lie
# furthest away from each other. If there are no two identical digrams inside S, your function should return -1.
#
# Examples:
# 1. Given S = "aabcaabcabda" your function should return 7.
# The furthest identical digrams are "ab"s, starting in positions 2 and 9 (enumerating from 1): "aabcaabcabda".
# 2. Given S = "aaa" your function should return 1. The furthest identical digrams are "aa"s starting at positions 1 and 2.
# 3. Given S = "codility" your function should return -1. There are no two identical digrams in S.
# Write an efficient algorithm for the following assumptions.


class Solution:
    def func(self, S: str) -> int:
        max_distance = -1
        for i in range(0, len(S) - 1):
            pattern = S[i:i + 2]
            for j in range(i + 1, len(S) - 1):
                if pattern == S[j:j + 2]:
                    max_distance = max(j - i, max_distance)

        return max_distance


sol = Solution()
sol.func(S="aabcaabcabda")
sol.func(S="aakmaakmakda")

sol.func(S="codility")
sol.func("")
