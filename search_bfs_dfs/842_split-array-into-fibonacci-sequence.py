# 842. Split Array into Fibonacci Sequence
# Medium
# Given a string S of digits, such as S = "123456579", we can split it into a Fibonacci-like sequence [123, 456, 579].
# Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:
# * 0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
# * F.length >= 3;
# * and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
# * Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes,
# except if the piece is the number 0 itself.
#
# Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.
#
# Example 1:
# Input: "123456579"
# Output: [123,456,579]
#
# Example 2:
# Input: "11235813"
# Output: [1,1,2,3,5,8,13]
#
# Example 3:
# Input: "112358130"
# Output: []
# Explanation: The task is impossible.
#
# Example 4:
# Input: "0123"
# Output: []
# Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
#
# Example 5:
# Input: "1101111"
# Output: [110, 1, 111]
# Explanation: The output [11, 0, 11, 11] would also be accepted.
#
# Note:
# 1 <= S.length <= 200
# S contains only digits.

from typing import List


class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        rslt = []
        start_idx = 0
        if self.dfs(S, start_idx, rslt):
            return rslt
        else:
            return []
    def dfs(self, s, idx, rslt):
        if idx == len(s) and len(rslt) >= 3:
            return True
        for i in range(idx, len(s)):
            if s[idx] == '0' and i > idx:
                break
            num = int(s[idx:i + 1])
            if num>=2**31:
                return False
            size = len(rslt)
            if size >= 2 and num > rslt[-1] + rslt[-2]:
                break
            if size <= 1 or num == rslt[-1] + rslt[-2]:
                rslt.append(int(num))
                if self.dfs(s, i + 1, rslt):
                    return True
                rslt.pop()
        return False


sol = Solution()
sol.splitIntoFibonacci(S="123456579")
