# 241. Different Ways to Add Parentheses
# Medium
#
# 2010
#
# 107
#
# Add to List
#
# Share
# Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.
#
# Example 1:
#
# Input: "2-1-1"
# Output: [0, 2]
# Explanation:
# ((2-1)-1) = 0
# (2-(1-1)) = 2
# Example 2:
#
# Input: "2*3-4*5"
# Output: [-34, -14, -10, -10, 10]
# Explanation:
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10
# Accepted
# 116.4K
# Submissions
# 203.8K
# Seen this question in a real interview before?

from typing import List


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        string_to_values = dict()
        temp = self.get_possible_results(s=input, string_to_values=string_to_values)

        return sorted(temp)
    def get_possible_results(self, s, string_to_values):
        if s in string_to_values.keys():
            return string_to_values[s]
        if self.is_numeric(s):
            string_to_values[s] = [int(s)]
            return string_to_values[s]

        total_rslt = list()

        for i in range(0, len(s)):
            if s[i] in ["+", "-", "*"]:
                left_rslts = self.get_possible_results(s[0:i],string_to_values)
                right_rslts = self.get_possible_results(s[i + 1:],string_to_values)

                for left_one_rslt in left_rslts:
                    for right_one_rslt in right_rslts:
                        temp_rslt = self.apply_binary_operation(left_one_rslt, right_one_rslt, s[i])
                        total_rslt.append(temp_rslt)
        return total_rslt

    def apply_binary_operation(self, num1, num2, operation):
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == "*":
            return num1 * num2
        else:
            raise Exception("invalid input")

    def is_numeric(self, s):
        for char in s:
            if char in ["+", "-", "*"]:
                return False
        return True

sol = Solution()
sol.diffWaysToCompute(input="2")

#sol.diffWaysToCompute(input="2*3-4*5")