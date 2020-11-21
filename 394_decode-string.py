# 394. Decode String
# Medium
#
# Given an encoded string, return its decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
#
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
#
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4]
#
# Example 1:
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
#
# Example 2:
# Input: s = "3[a2[c]]"
# Output: "accaccacc"
#
# Example 3:
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
#
# Example 4:
# Input: s = "abc3[cd]xyz"
# Output: "abccdcdcdxyz"
#
# Constraints:
# * 1 <= s.length <= 30
# * s consists of lowercase English letters, digits, and square brackets '[]'.
# * s is guaranteed to be a valid input.
# * All the integers in s are in the range [1, 300].


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        n = len(s)
        i = 0
        while i < n:
            # we see a number, we get the whole number and push it to stack
            if s[i].isdigit():
                num_in_str_arr = []
                while i<n and s[i].isdigit():
                    num_in_str_arr.append(s[i])
                    i += 1
                stack.append(int(''.join(num_in_str_arr)))
            elif s[i] == '[':
                stack.append('[')
                i += 1
            # if we see letter, we get he whole word and push it to stack
            elif s[i].isalpha():
                letter_arr = []
                while i<n and s[i].isalpha():
                    letter_arr.append(s[i])
                    i += 1
                stack.append(''.join(letter_arr))

            elif s[i] == ']':
                i += 1
                words_arr = []
                while stack[-1] != '[':
                    words_arr.append(stack.pop())
                # pop out the '['
                assert stack.pop() == '['
                letters = ''.join(reversed(words_arr))
                num = stack.pop()
                stack.append(letters * num)

        rslt = ''.join(stack)
        return rslt


sol = Solution()
s = "3[a2[c]]"
sol.decodeString(s=s)

s = "2[abc]3[cd]ef"
sol.decodeString(s=s)
