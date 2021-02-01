# 204. Count Primes
# Easy

# Add to List
#
# Share
# Count the number of prime numbers less than a non-negative number, n.
#
# Example 1:
# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
#
# Example 2:
# Input: n = 0
# Output: 0
#
# Example 3:
# Input: n = 1
# Output: 0

import math


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0

        is_prime = [True] * (n)
        # 0 is not Prime
        is_prime[0] = False
        # 1 is not prime
        is_prime[1] = False
        # less than n, consider at most n-1
        for num in range(2, n):
            if not is_prime[num]:
                continue
            factor = 2
            while num * factor < n:
                is_prime[num * factor] = False
                factor += 1

        rslt = []
        for i in range(len(is_prime)):
            if is_prime[i]:
                rslt.append(i)

        return len(rslt)


sol = Solution()
sol.countPrimes(n=10)
