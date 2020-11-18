# 845. Longest Mountain in Array
# Medium
#
# Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:
#
# * B.length >= 3
# * There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
#
# (Note that B could be any subarray of A, including the entire array A.)
# Given an array A of integers, return the length of the longest mountain.
#
# Return 0 if there is no mountain.
#
# Example 1:
# Input: [2,1,4,7,3,2,5]
# Output: 5
# Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
#
# Example 2:
# Input: [2,2,2]
# Output: 0
# Explanation: There is no mountain.
#
# Note:
# * 0 <= A.length <= 10000
# * 0 <= A[i] <= 10000
#
# Follow up:
# Can you solve it using only one pass?
# Can you solve it in O(1) space?

from typing import List


class Solution:
    # two pointers
    #  L = 左山脚， R = 右山脚
    def longestMountain(self, A: List[int]) -> int:
        n = len(A)
        res = l = 0
        while l + 2 < n:
            r = l + 1
            # fix 左山脚
            if A[l] < A[l + 1]:
                # 移动右指针找山顶
                while r + 1 < n and A[r] < A[r + 1]:
                    r += 1
                # 移动右指针找山脚
                if r < n - 1 and A[r] > A[r + 1]:
                    while r + 1 < n and A[r] > A[r + 1]:
                        r += 1
                    # 更新结果
                    res = max(res, r - l + 1)
                else:
                    r += 1
            l = r

        return res


# wrong
class Solution2:
    def longestMountain(self, A: List[int]) -> int:
        n = len(A)
        if n < 3:
            return 0
        # inc[i], the max length of increasing sequence ending at A[i]
        inc = [0 for _ in range(n)]
        # des[i], the max length of the decreasing sequence starting at A[i]
        des = [0 for _ in range(n)]

        for i in range(1, n):
            if A[i] > A[i - 1]:
                inc[i] = inc[i - 1] + 1
        for i in reversed(range(n - 1)):
            if A[i] > A[i + 1]:
                des[i] = des[i + 1] + 1
        ans = 0
        for i in range(0, n):
            ans = max(ans, des[i] + inc[i] + 1)

        if ans >= 3:
            return ans
        else:
            return 0


sol = Solution()
A = [2, 1, 4, 7, 3, 2, 5]
sol.longestMountain(A)

A = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
sol.longestMountain(A=A)
