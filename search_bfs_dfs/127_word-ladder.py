# 127. Word Ladder
# Medium
#
# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
# 1. Only one letter can be changed at a time.
# 2. Each transformed word must exist in the word list.
#
# Note:
# 1. Return 0 if there is no such transformation sequence.
# 2. All words have the same length.
# 3. All words contain only lowercase alphabetic characters.
# 4. You may assume no duplicates in the word list.
# 5. You may assume beginWord and endWord are non-empty and are not the same.
#
# Example 1:
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
#
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
#
# Example 2:
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

from collections import deque

from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # solve using bfs algorithm
        q = deque()
        q.append(beginWord)
        visited = set()
        visited.add(beginWord)
        distance = 0
        while q:
            distance += 1
            for _ in range(len(q)):
                curr_word = q.popleft()
                if curr_word == endWord:
                    return distance
                for next_word in self.get_one_char_change_words(word=curr_word):
                    if (next_word in wordList or next_word == endWord) and (next_word not in visited):
                        q.append(next_word)
                        visited.add(next_word)
            
        return 0

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
sol.ladderLength(beginWord, endWord,wordList)