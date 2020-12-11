# 1015. Smallest Integer Divisible by K
# Medium
# Given a positive integer K, you need to find the length of the smallest positive integer N such that N is divisible by K, and N only contains the digit 1.
#
# Return the length of N. If there is no such N, return -1.
#
# Note: N may not fit in a 64-bit signed integer.
#
# Example 1:
# Input: K = 1
# Output: 1
# Explanation: The smallest answer is N = 1, which has length 1.
#
# Example 2:
# Input: K = 2
# Output: -1
# Explanation: There is no such positive integer N divisible by 2.
#
# Example 3:
# Input: K = 3
# Output: 3
# Explanation: The smallest answer is N = 111, which has length 3.
#
# Constraints:
# 1 <= K <= 105

# 思路显然是暴力枚举.
#
# 但是两个问题:
#
# 1. 当1的位数非常大时, 模运算很费时间, 会超时.
#
# 其实每次不用完全用 '11111...' 来 % K, 上一次的余数 * 10 + 1 后再 % K就行.
#
# 证明:
#
# 令f(n) = 111111...(n个1);　　
#
# 　g(n) = f(n) % K
#
# 　因为f(n) = f(n - 1) * 10 + 1
#
# 　所以f(n) % K = (f(n - 1) * 10 + 1) % K
#
# 　即g(n) = g(n - 1) * 10 + 1
#
# 2.枚举何时停止?
# 一种方法是可以设置一个大数, 比如10的6次方, 可以Accepted.
#
# 更精确的方法是: 从1个1到K个1, 如果这里都没有答案, 后面也没了.
#
# 因为K的余数不包括0的话有K - 1
# 个, 我们算了K个, K个里面没有0的话, 里面必然至少有两个相等的(抽屉原理), 而根据第一个问题所示, 相邻的余数有关系, 所以一相等之后就是重复循环这些数了, 前面找不到后面也肯定没有了.例如K = 6:
#
# 1 % 6 = 1
# 11 % 6 = 5
# 111 % 6 = 3
# 1111 % 6 = 1
# 11111 % 6 = 5
# 111111 % 6 = 3

class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0:
            return -1
        g = 0
        for i in range(1, K+1):
            g = (g * 10 + 1) % K
            if g == 0:
                return i
        return -1