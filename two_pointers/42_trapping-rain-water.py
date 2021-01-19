# 42. Trapping Rain Water
# Hard
#
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much
# water it can trap after raining.
#
# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
#
# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9
#
# Constraints:
# n == height.length
# 0 <= n <= 3 * 104
# 0 <= height[i] <= 105

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # left_max[i] = maximum height from height[0], height[1].....height[i[
        # right_max[i] = maximum height from height[-1], ...all the way to height[i]

        left_max = [0] * len(height)
        right_max = [0] * len(height)

        for i, h in enumerate(height):
            if i == 0:
                left_max[i] = h
                continue
            left_max[i] = max(left_max[i - 1], h)

        for i in reversed(range(len(height))):
            if i == len(height) - 1:
                right_max[i] = height[i]
                continue
            right_max[i] = max(right_max[i + 1], height[i])

        rain = 0
        for i in range(len(height)):
            rain += min(left_max[i], right_max[i]) - height[i]

        return rain


sol = Solution()
sol.trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
