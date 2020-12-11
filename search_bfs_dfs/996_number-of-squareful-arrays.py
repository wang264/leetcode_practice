# 996. Number of Squareful Arrays
# Hard
#
# Given an array A of non-negative integers, the array is squareful if for every pair of adjacent elements, their sum is a perfect square.
# Return the number of permutations of A that are squareful.  Two permutations A1 and A2 differ if and only if there is some index i such that A1[i] != A2[i].
#
# Example 1:
# Input: [1,17,8]
# Output: 2
# Explanation:
# [1,8,17] and [17,8,1] are the valid permutations.
#
# Example 2:
# Input: [2,2,2]
# Output: 1
#
# Note:
# 1 <= A.length <= 12
# 0 <= A[i] <= 1e9
import math

from typing import List


class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        squareful_set = self.generate_is_squareful_dic(A=A)
        curr_path = []
        rslt = []
        A = sorted(A)
        selected = [False for _ in range(len(A))]
        self.dfs(A, curr_path, rslt, selected, squareful_set)
        return len(rslt)

    def dfs(self, A, curr_path, rslt, selected, squareful_set):
        n = len(A)
        if len(curr_path) == n:
            rslt.append(curr_path[:])

        for i in range(0, n):
            if selected[i]:
                continue
            if len(curr_path) > 0 and ((curr_path[-1], A[i]) not in squareful_set):
                continue
            # 1 1' 1'' 2 2' 2'' 2'''.... need to select 1 and 1' before we select 1''
            if i > 0 and A[i - 1] == A[i] and (not selected[i - 1]):
                continue
            selected[i] = True
            curr_path.append(A[i])
            self.dfs(A, curr_path, rslt, selected, squareful_set)
            curr_path.pop()
            selected[i] = False

    def generate_is_squareful_dic(self, A: List[int]):
        is_squareful_set = set()
        l = sorted(list(set(A)))
        for i in range(len(l)):
            for j in range(i, len(l)):
                is_squareful = int(math.pow(l[i] + l[j], 0.5)) ** 2 == l[i] + l[j]
                if is_squareful:
                    is_squareful_set.add((l[i], l[j]))
                    is_squareful_set.add((l[j], l[i]))
        return is_squareful_set


sol = Solution()
sol.numSquarefulPerms(A=[2,2,2])
