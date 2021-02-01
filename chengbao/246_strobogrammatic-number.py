# [LeetCode] 246. Strobogrammatic Number 对称数
#
# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
#
# Write a function to determine if a number is strobogrammatic. The number is represented as a string.
#
# Example 1:
#
# Input:  "69"
# Output: true
# Example 2:
#
# Input:  "88"
# Output: true
# Example 3:
#
# Input:  "962"
# Output: false
#
# 这道题定义了一种对称数，就是说一个数字旋转 180 度和原来一样，也就是倒过来看一样，比如 609，倒过来还是 609 等等，满足这种条件的数字其实没
# 有几个，只有 0,1,8,6,9。这道题其实可以看做求回文数的一种特殊情况，还是用双指针来检测，首尾两个数字如果相等的话，
# 只有它们是 0,1,8 中间的一个才行，如果它们不相等的话，必须一个是6一个是9，或者一个是9一个是6，其他所有情况均返回 false，参见代码如下；


class Solution:
    def isStrobogrammatic(self, num: str):
        left = 0
        right = len(num) - 1

        while left <= right:
            if num[left] == num[right]:
                if num[left] not in ['1', '0', '8']:
                    return False
            else:
                if not ((num[left] == '9' and num[right] == '6') or (num[left] == '6' and num[right] == '9')):
                    return False
            left += 1
            right -= 1

        return True

sol = Solution()
sol.isStrobogrammatic(num='962')
sol.isStrobogrammatic(num='619')