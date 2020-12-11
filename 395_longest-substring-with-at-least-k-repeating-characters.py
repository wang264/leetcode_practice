# 395. Longest Substring with At Least K Repeating Characters
# Medium
# Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k
#
# Example 1:
# Input: s = "aaabb", k = 3
# Output: 3
# Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
#
# Example 2:
# Input: s = "ababbc", k = 2
# Output: 5
# Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
#
# Constraints:
# 1 <= s.length <= 104
# s consists of only lowercase English letters.
# 1 <= k <= 105
#
# 1.如果字符串s的长度少于k，那么一定不存在满足题意的子字符串，返回0；
# 2.如果一个字符在s中出现的次数少于k次，那么所有的包含这个字符的子字符串都不能满足题意。所以，应该去不包含这个字符的子字符串继续寻找。这就是分而治之的思路，返回不同子串的长度最大值。
# 3.如果s中的每个字符出现的次数都大于k次，那么s就是我们要求的字符串。

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)

