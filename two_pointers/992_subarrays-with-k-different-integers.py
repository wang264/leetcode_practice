# 992. Subarrays with K Different Integers
# Hard
#
# Given an array A of positive integers, call a (contiguous, not necessarily distinct)
# subarray of A good if the number of different integers in that subarray is exactly K.
#
# (For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)
#
# Return the number of good subarrays of A.
#
# Example 1:
# Input: A = [1,2,1,2,3], K = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
#
# Example 2:
# Input: A = [1,2,1,3,4], K = 3
# Output: 3
# Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
#
# Note:
# 1 <= A.length <= 20000
# 1 <= A[i] <= A.length
# 1 <= K <= A.length

from typing import List

"""
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        if len(A) < 2:
            return 0
        if len(A) == 2:
            return 1 if A[0] != A[1] else 0

        rslt = []
        curr_sub_arr = []
        num_to_count = dict()
        # when we move left from zero to larger...
        # right can only be larger than left.....
        right = 0
        for left in range(len(A) - 1):
            if left == 0:
                pass
            elif num_to_count[A[left - 1]] == 1:
                del num_to_count[A[left - 1]]
            else:
                num_to_count[A[left - 1]] -= 1

            while right < len(A) and len(num_to_count.keys()) <= K:
                if A[right] not in num_to_count.keys():
                    num_to_count[A[right]] = 0

                num_to_count[A[right]] += 1

                curr_sub_arr.append(A[right])
                if len(num_to_count.keys()) == K:
                    rslt.append(curr_sub_arr[:])
                if right<len(A)-1 and len(num_to_count.keys())==K and A[right+1] not in num_to_count.keys()
                    break
                right += 1

        return rslt


sol = Solution()
sol.subarraysWithKDistinct(A=[1, 1, 2, 2, 3, 1, 2, 3], K=2)
"""

