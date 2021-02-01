# 189. Rotate Array
# Medium
#
# Given an array, rotate the array to the right by k steps, where k is non-negative.
#
#
# Follow up:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
# Could you do it in-place with O(1) extra space?
#
#
# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:
#
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
#
# Constraints:
# 1 <= nums.length <= 2 * 104
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105

from typing import List


class Solution:
    # 还需要一个变量 start，这个是为了防止陷入死循环的，初始化为0，一旦当
    # idx 变到了 strat 的位置，则 start 自增1，再赋值给 idx，这样 idx
    # 的位置也改变了，可以继续进行交换了。举个例子，假如[1, 2, 3, 4], K = 2
    # 的话，那么 idx = 0，下一次变为 idx = (idx + k) % n = 2，再下一次又变成了
    # idx = (idx + k) % n = 0，此时明显 1 和 3 的位置还没有处理过，所以当我们发现
    # idx 和 start 相等，则二者均自增1，那么此时 idx = 1，下一次变为
    # idx = (idx + k) % n = 3，就可以交换完所有的数字了。
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k%len(nums)==0 or len(nums)<=1:
            return

        idx_temp = 0
        n = len(nums)
        val_temp = nums[0]
        start = 0
        for _ in range(len(nums)):
            from_idx = idx_temp
            correct_val = val_temp
            to_idx = ( from_idx + k) % n
            if to_idx == start:
                start += 1
                idx_temp = to_idx + 1
                val_temp = nums[idx_temp]

            else:
                idx_temp = to_idx
                val_temp = nums[idx_temp]

            nums[to_idx] = correct_val


sol = Solution()
a = [1, 2, 3, 4, 5, 6, 7]
sol.rotate(a, 2)
a

b = [1, 2, 3, 4]
sol.rotate(b, 2)
b

b = [1, 2]
sol.rotate(b, 2)
