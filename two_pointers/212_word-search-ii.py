# 212. Word Search II
# Hard
# Given an m x n board of characters and a list of strings words, return all words on the board.
#
# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally
# or vertically neighboring. The same letter cell may not be used more than once in a word.
#
# Example 1:
# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
#
# Example 2:
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
#
# Constraints:
# *   m == board.length
# *   n == board[i].length
# *   1 <= m, n <= 12
# *   board[i][j] is a lowercase English letter.
# *   1 <= words.length <= 3 * 104
# *   1 <= words[i].length <= 10
# *   words[i] consists of lowercase English letters.
# *   All the strings of words are unique.

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_word = False
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children.keys():
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_word = True
        node.word = word

    # return the node that contain the word
    def find(self, word):
        node = self.root
        for char in word:
            node = node.children.get(char)
            if node is None:
                return None

        return node

    # check if the word exist in Trie
    def search_word(self, word):
        node = self.find(word)
        if node is None:
            return False
        else:
            return node.is_word


from typing import List

DELTAS = {(0, 1), (1, 0), (0, -1), (-1, 0)}


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        rows = len(board)
        cols = len(board[0])
        visited = set()
        rslt = set()
        for row in range(rows):
            for col in range(cols):
                visited.add((row, col))
                char = board[row][col]
                self.dfs_search(board, row, col, trie.root.children.get(char), visited, rslt)
                visited.remove((row, col))

        return list(rslt)

    def dfs_search(self, board, row, col, node: TrieNode, visited, rslt):
        if node is None:
            return
        if node.is_word:
            rslt.add(node.word)

        for d_row, d_col in DELTAS:
            next_row = d_row + row
            next_col = d_col + col

            if (next_row, next_col) in visited or (not self.is_valid(board, next_row, next_col)):
                continue
            visited.add((next_row, next_col))
            next_char = board[next_row][next_col]
            self.dfs_search(board, next_row, next_col, node.children.get(next_char), visited, rslt)
            visited.remove((next_row, next_col))

    def is_valid(self, board, row, col):
        num_rows = len(board)
        num_cols = len(board[0])

        return 0 <= row < num_rows and 0 <= col < num_cols


sol = Solution()
# sol.findWords(board=[["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
#               words=["oath", "pea", "eat", "rain"])

sol.findWords(board=[['a', 'b'], ['c', 'd']], words=['a', 'cd'])
