# 1048. Longest String Chain
# Medium
#
# You are given an array of words where each word consists of lowercase English letters.
#
# wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without
# changing the order of the other characters to make it equal to wordB.
#
# For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
# A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor
# of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.
#
# Return the length of the longest possible word chain with words chosen from the given list of words.

# Example 1:
# Input: words = ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
#
# Example 2:
# Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
# Output: 5
# Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
#
# Example 3:
# Input: words = ["abcd","dbqca"]
# Output: 1
# Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
# ["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.

# Constraints:
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 16
# words[i] only consists of lowercase English letters.

from typing import List


# dp[i] := max length of chain of (A[0] ~ A[i-1])

# dp[i] = max{dp[j] + 1} if A[j] is predesessor of A[i], 1 <= j <i

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        words.sort(key=len)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if self.valid(short=words[j], long=words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    def valid(self, short, long):
        if len(short) + 1 != len(long):
            return False
        # select char to remove
        for loc in range(len(long)):
            delete_one_char = long[0:loc] + long[loc + 1:]
            if delete_one_char == short:
                return True

        return False


sol = Solution()
sol.longestStrChain(words=["a", "b", "ba", "bca", "bda", "bdca"])

