# 49. Group Anagrams
# Medium
#
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically
# using all the original letters exactly once.
#
# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
# Example 2:
# Input: strs = [""]
# Output: [[""]]
#
# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
#
# Constraints:
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lower-case English letters.

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashkey_to_values = dict()
        for s in strs:
            hash_result = self.hash(s)
            if hash_result not in hashkey_to_values.keys():
                hashkey_to_values[hash_result] = []
            hashkey_to_values[hash_result].append(s)

        return list(hashkey_to_values.values())

    def hash(self, s):
        arr = [0] * 26
        for char in s:
            arr[ord(char) - ord('a')] += 1

        return ''.join([str(integer) for integer in arr])


sol = Solution()
sol.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"])
