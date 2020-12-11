# 227. Basic Calculator II
# Medium
# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.
#
# Example 1:
#
# Input: "3+2*2"
# Output: 7
# Example 2:
#
# Input: " 3/2 "
# Output: 1
# Example 3:
#
# Input: " 3+5 / 2 "
# Output: 5
# Note:
#
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curr_number = 0
        i = 0
        n = len(s)
        operation = '+'
        while i < n:
            if s[i] == ' ':
                i += 1
                continue
            # try to get the whole number

            while i < n and s[i].isdigit():
                curr_number = curr_number * 10 + int(s[i])
                i+=1

            if operation in '+-':
                stack.append(curr_number * (1 if operation == '+' else -1))
            elif operation == '*':
                stack[-1] *= curr_number
            elif operation == '/':
                sign = -1 if stack[-1] < 0 or curr_number < 0 else 1
                stack[-1] = abs(stack[-1]) // abs(curr_number) * sign
            curr_number = 0
            if i < n:
                operation = s[i]
            i += 1
        return sum(stack)

sol = Solution()
sol.calculate(s='3+2*2')
