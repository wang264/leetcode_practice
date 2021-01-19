# 875. Koko Eating Bananas
# Medium
#
# Koko loves to eat bananas.  There are N piles of bananas, the i-th pile has piles[i] bananas.
# The guards have gone and will come back in H hours.
#
# Koko can decide her bananas-per-hour eating speed of K.  Each hour, she chooses some pile of bananas,
# and eats K bananas from that pile.  If the pile has less than K bananas, she eats all of them instead,
# and won't eat any more bananas during this hour.
#
# Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.
#
# Return the minimum integer K such that she can eat all the bananas within H hours.
#
# Example 1:
# Input: piles = [3,6,7,11], H = 8
# Output: 4
#
# Example 2:
# Input: piles = [30,11,23,4,20], H = 5
# Output: 30
#
# Example 3:
# Input: piles = [30,11,23,4,20], H = 6
# Output: 23
#
# Constraints:
# 1 <= piles.length <= 10^4
# piles.length <= H <= 10^9
# 1 <= piles[i] <= 10^9

from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        left = 1
        right = max(piles)

        while left + 1 < right:
            mid = (left + right) // 2
            # eat too fast
            if self.calc_eat_time(piles, K=mid) < H:
                right = mid
            # ear too slow
            elif self.calc_eat_time(piles, K=mid) > H:
                left = mid
            # if equal, we could try eat slower
            else:
                right = mid

        if self.calc_eat_time(piles, K=left) <= H:
            return left
        else:
            return right

    def calc_eat_time(self, piles, K) -> int:
        hour = 0
        for pile in piles:
            if K == 1:
                hour += pile
                continue
            if K == pile:
                hour += 1
                continue
            hour += pile // K + 1
        return hour


sol = Solution()
sol.minEatingSpeed(piles=[30, 11, 23, 4, 20], H=5)

sol.minEatingSpeed(piles=[30, 11, 23, 4, 20], H=6)


sol.minEatingSpeed(piles=[312884470], H=968709470)