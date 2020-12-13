# 126. Word Ladder II
# Hard
#
# Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:
#
# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:
#
# Return an empty list if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.

# Example 1:
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# Output:
# [
#   ["hit","hot","dot","dog","cog"],
#   ["hit","hot","lot","log","cog"]
# ]

# Example 2:
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: []
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

from typing import List


# we solve it using dfs, this method time limit exceed.
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        rslt = []
        curr_list = [beginWord]
        visited = set()
        visited.add(beginWord)
        self.dfs_helper(beginWord, curr_list, endWord, wordList, visited,rslt)
        return rslt

    def dfs_helper(self, curr_word, curr_list, end_word, word_list, visited, rslt):
        if curr_word == end_word:
            if len(rslt)==0:
                rslt.append(curr_list[:])
                return
            if len(curr_list) == len(rslt[0]):
                rslt.append(curr_list[:])
                return

            if len(curr_list) < len(rslt[0]):
                rslt.clear()
                rslt.append(curr_list[:])
                return


        if len(rslt)>0 and len(curr_list)>len(rslt[0]):
            return

        for next_word in self.get_one_char_change_words(curr_word):
            if (next_word in word_list or next_word==end_word) and (next_word not in visited):
                curr_list.append(next_word)
                visited.add(next_word)
                self.dfs_helper(next_word, curr_list, end_word, word_list, visited, rslt)
                visited.remove(next_word)
                curr_list.pop()

    def get_one_char_change_words(self, word):
        # the index that point to the character that need to change.
        words = []
        for idx in range(len(word)):
            left = word[0:idx]
            right = word[idx + 1:]

            for char in "abcdefghijklmnopqrstuvwxyz":
                if char == word[idx]:
                    continue
                words.append(left + char + right)

        return words


sol = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

sol.findLadders(beginWord, endWord, wordList)
