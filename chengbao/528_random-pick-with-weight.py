# 528. Random Pick with Weight
# Medium
#
# You are given an array of positive integers w where w[i] describes the weight of ith index (0-indexed).
#
# We need to call the function pickIndex() which randomly returns an integer in the range [0, w.length - 1]. pickIndex() should return the integer proportional to its weight in the w array. For example, for w = [1, 3], the probability of picking the index 0 is 1 / (1 + 3) = 0.25 (i.e 25%) while the probability of picking the index 1 is 3 / (1 + 3) = 0.75 (i.e 75%).
#
# More formally, the probability of picking index i is w[i] / sum(w).
#
#
# Example 1:
# Input
# ["Solution","pickIndex"]
# [[[1]],[]]
# Output
# [null,0]
#
# Explanation
# Solution solution = new Solution([1]);
# solution.pickIndex(); // return 0. Since there is only one single element on the array the only option is to return the first element.
#
# Example 2:
# Input
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# Output
# [null,1,1,1,1,0]
#
# Explanation
# Solution solution = new Solution([1, 3]);
# solution.pickIndex(); // return 1. It's returning the second element (index = 1) that has probability of 3/4.
# solution.pickIndex(); // return 1
# solution.pickIndex(); // return 1
# solution.pickIndex(); // return 1
# solution.pickIndex(); // return 0. It's returning the first element (index = 0) that has probability of 1/4.
#
# Since this is a randomization problem, multiple answers are allowed so the following outputs can be considered correct :
# [null,1,1,1,1,0]
# [null,1,1,1,1,1]
# [null,1,1,1,0,0]
# [null,1,1,1,0,1]
# [null,1,0,1,0,0]
# ......
# and so on.
#
# Constraints:
# 1 <= w.length <= 10000
# 1 <= w[i] <= 10^5
# pickIndex will be called at most 10000 times.

from typing import List
import random
class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = [None]*len(w)
        self.prefix_sum[0] = w[0]

        for i in range(1, len(w)):
            self.prefix_sum[i]=self.prefix_sum[i-1]+w[i]

    def pickIndex(self) -> int:
        if len(self.prefix_sum)==1:
            return 0

        rand_num = random.randint(a=0,b=self.prefix_sum[-1])
        return self._bisect_right(arr=self.prefix_sum,target=rand_num)
    # try to find the target and return the index.
    # if does not exist, then return the index of smallest number exist, and that number
    # is larger than target.
    def _bisect_right(self,arr,target):
        left = 0
        right =len(arr)-1

        while left+1<right:
            mid = (left+right)//2
            if arr[mid]<target:
                left = mid
            elif arr[mid]>target:
                right = mid
            else:
                return mid

        # in here we have left< right and we can not find target.
        if arr[left]>=target:
            return left
        elif arr[right]>=target:
            return right



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

sol = Solution(w=[1,3])

for i in range(1000):
    print(sol.pickIndex())

sol._bisect_right(arr=[1,4],target=1)
