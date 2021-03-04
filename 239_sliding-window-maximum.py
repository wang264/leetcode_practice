# 239. Sliding Window Maximum
# Hard
#
# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of
# the array to the very right. You can only see the k numbers in the window. Each time the sliding
# window moves right by one position.
# Return the max sliding window.
#
# Example 1:
#
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]
# Example 3:
#
# Input: nums = [1,-1], k = 1
# Output: [1,-1]
# Example 4:
#
# Input: nums = [9,11], k = 2
# Output: [11]
# Example 5:
#
# Input: nums = [4,-2], k = 2
# Output: [4]
#
# Constraints:
#
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length

import collections
from typing import List


class MaxQueue:
    def __init__(self):
        self.q_ = collections.deque()

    # push to the queue, and pop any element that smaller than it
    def push(self, element):
        while self.q_ and element > self.q_[-1]:
            self.q_.pop()
        self.q_.append(element)

    def pop(self):
        self.q_.popleft()

    def max(self):
        return self.q_[0]


m = MaxQueue()
m.push(2)


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = MaxQueue()
        ans = []
        for i in range(len(nums)):
            q.push(nums[i])
            # have enough element in the window
            if i >= k - 1:
                ans.append(q.max())
                # if the element we need to kick out
                if nums[i - k + 1] == q.max():
                    q.pop()

        return ans


sol = Solution()
sol.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3)
