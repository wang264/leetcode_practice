# 69. Sqrt(x)
# Easy
#
# Given a non-negative integer x, compute and return the square root of x.
#
# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
#
# Example 1:
# Input: x = 4
# Output: 2
#
# Example 2:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
#
# Constraints:
# 0 <= x <= 231 - 1


class Solution:
    def mySqrt(self, x: int) -> int:
        # write your code here
        left = 0
        right = x
        while left + 1 < right:
            mid = (left + right) // 2
            if mid * mid < x:
                left = mid
            elif mid * mid > x:
                right = mid
            else:
                return mid

        if right * right <= x:
            return right
        else:
            return left


sol = Solution()
sol.mySqrt(8)
