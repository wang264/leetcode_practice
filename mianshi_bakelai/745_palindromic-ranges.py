# 回文的范围 · Palindromic Ranges
# 字符串
# Palindrome
# 谷歌
# 描述
# A positive integer is a palindrome if its decimal representation (without leading zeros) is a palindromic string
# (a string that reads the same forwards and backwards). For example, the numbers 5, 77, 363, 4884, 11111, 12121
# and 349943 are palindromes.
#
# A range of integers is interesting if it contains an even number of palindromes. The range [L, R], with L <= R,
# is defined as the sequence of integers from L to R (inclusive): (L, L+1, L+2, …, R-1, R). L and R are the range’s
# first and last numbers.
#
# The range [L1, R1] is a subrange of [L, R] if L <= L1 <= R1 <= R. Your job is to determine how many interesting
# subranges of [L, R] there are.
#
# Data guarantee results in the range of int, and will not overflow
# 样例
# Example 1:
#
# Input : L = 1, R = 2
# Output : 1
# Example 2:
#
# Input : L = 1, R = 7
# Output : 12
# Example 3:
#
# Input : L = 87, R = 88
# Output : 1
class Solution:
    """
    @param L: A positive integer
    @param R: A positive integer
    @return:  the number of interesting subranges of [L,R]
    """

    def PalindromicRanges(self, L, R):
        if R < L:
            return 0
        if R == L:
            return 1  # zero palindrome is also a solution
        # 1. use an array to store all palindromes between L and R;
        # use R-L+2, to include 0 and len+1 (i.e. prefix sum for L and R)
        # [L,L] [L,L+1].......[L,R]
        # L=3 R = 7
        #    [XXX][3,3],[3,4],[3,5],[3,6],[3,7]   range(0,R-L+2)
        # idx= 0    1     2      3    4     5
        # val= 0    1     2      3    4     5

        prefix_sum = [0 for _ in range(R - L + 2)]  # accumulation of palidrome counts
        for i in range(L, R + 1):
            prefix_sum[i - L + 1] = prefix_sum[i - L]  # accumulate previous value
            if self.is_pali(i):
                prefix_sum[i - L + 1] += 1
        # 2. use O(n^2) to check every case
        count = 0
        for i in range(1, R - L + 2):  # right
            for j in reversed(list(range(0, i))): # left
                if (prefix_sum[i] - prefix_sum[j]) % 2 == 0:
                    count += 1
        return count

    def is_pali(self, n):
        reversed = 0
        number = n
        while number != 0:
            k = number % 10
            reversed = reversed * 10 + k
            number = number // 10

        return reversed == n


sol = Solution()
sol.PalindromicRanges(L=1,R=7)