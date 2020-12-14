# 241. Different Ways to Add Parentheses
# Medium
#
# Given a string of numbers and operators, return all possible results from computing all the different possible
# ways to group numbers and operators. The valid operators are +, - and *.
#
# Example 1:
# Input: "2-1-1"
# Output: [0, 2]
# Explanation:
# ((2-1)-1) = 0
# (2-(1-1)) = 2
#
# Example 2:
# Input: "2*3-4*5"
# Output: [-34, -14, -10, -10, 10]
# Explanation:
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10

from typing import List


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        dic = dict()
        return sorted(self.possible_results(s=input, dic=dic))

    def possible_results(self, s: str, dic: dict):
        if s in dic.keys():
            return dic[s]

        if self.is_number(s):
            dic[s] = [int(s)]
            return dic[s]
        # find all possible ways to split
        rslt = list()
        for i in range(len(s)):
            if s[i] in ["+","-","*"]:
                rslt_left = self.possible_results(s[0:i],dic)
                rslt_right = self.possible_results(s[i+1:],dic)

                for a in rslt_left:
                    for b in rslt_right:
                        rslt.append(self.binary_operation(a,b,s[i]))

        dic[s] = list(rslt)
        return dic[s]


    def binary_operation(self, a, b, operator):
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b

    def is_number(self, s):
        for i in range(len(s)):
            if s[i] in ["+", "-", "*"]:
                return False

        return True


sol =Solution()
sol.diffWaysToCompute(input="2*3-4*5")
