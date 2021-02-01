# 1048. Longest String Chain
# Medium
#
# Given a list of words, each word consists of English lowercase letters.
#
# Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".
#
# A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.
#
# Return the longest possible length of a word chain with words chosen from the given list of words.
#
# Example 1:
# Input: words = ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: One of the longest word chain is "a","ba","bda","bdca".
#
# Example 2:
# Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
# Output: 5
#
# Constraints:
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 16
# words[i] only consists of English lowercase letters.

from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=len, reverse=True)
        # the length of the chain
        chain_len = [None] * len(words)
        n = len(words)
        for i in range(n):
            # does not exist longer words to convert to this word
            if chain_len[i] is None:
                chain_len[i] = 1
            for j in range(i + 1, n):
                if self.is_predecessor(w_longer=words[i], w_shorter=words[j]):
                    if chain_len[j] is None:
                        chain_len[j] = chain_len[i] + 1
                    else:
                        # for example,"ab" could come from
                        # 1.   "abdd"-->"abd"-->"ab"
                        # 2.   "abc"--->"ab"
                        chain_len[j] = max(chain_len[j], chain_len[i] + 1)
        return max(chain_len)

    def is_predecessor(self, w_longer, w_shorter):
        if len(w_longer) - len(w_shorter) != 1:
            return False
        n = len(w_longer)
        for i in range(0, n):
            temp_word = w_longer[0:i] + w_longer[i + 1:]
            if temp_word == w_shorter:
                return True

        return False


sol = Solution()
assert sol.longestStrChain(words=["a", "ab", "ac", "bd", "abc", "abd", "abdd"]) == 4
