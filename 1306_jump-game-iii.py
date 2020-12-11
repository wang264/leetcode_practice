# 1306. Jump Game III
# Medium
#
# Given an array of non-negative integers arr, you are initially positioned at start index
# of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i],
# check if you can reach to any index with value 0.
# Notice that you can not jump outside of the array at any time.
#
# Example 1:
# Input: arr = [4,2,3,0,3,1,2], start = 5
# Output: true
# Explanation:
# All possible ways to reach at index 3 with value 0 are:
# index 5 -> index 4 -> index 1 -> index 3
# index 5 -> index 6 -> index 4 -> index 1 -> index 3
#
# Example 2:
# Input: arr = [4,2,3,0,3,1,2], start = 0
# Output: true
# Explanation:
# One possible way to reach at index 3 with value 0 is:
# index 0 -> index 4 -> index 1 -> index 3
#
# Example 3:
# Input: arr = [3,0,2,1,2], start = 2
# Output: false
# Explanation: There is no way to reach at index 1 with value 0.
#
# Constraints:
# 1 <= arr.length <= 5 * 10 ^ 4
# 0 <= arr[i] < arr.length
# 0 <= start < arr.length

from typing import List

# solution using DFS
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # if index is valid, and we have not visit it before
        if 0 <= start < len(arr) and arr[start] >= 0:
            if arr[start] == 0:
                return True
            arr[start] = -1*arr[start]

            return self.canReach(arr,start+arr[start]) or self.canReach(arr,start-arr[start])


# solution using BFS
class Solution2:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        q = [start]

        while q:
            node = q.pop(0)
            # check if reach zero
            if arr[node] == 0:
                return True
            if arr[node] < 0:
                continue

            # check available next steps
            for i in [node + arr[node], node - arr[node]]:
                if 0 <= i < n:
                    q.append(i)

            # mark as visited
            arr[node] = -arr[node]

        return False

