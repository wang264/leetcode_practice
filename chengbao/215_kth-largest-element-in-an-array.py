# 215. Kth Largest Element in an Array
# Medium
# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Example 1:
#
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# Example 2:
#
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # if an array had length n. if k<=n
        # then the kth largest is the n-k+1 smallest.
        # if sorted, then n-k+1 smallest is the number with index n-k
        return self.select_kth_smallest(nums, len(nums) - k + 1)

    def select_kth_smallest(self, nums, k):
        # kth smallest, index with k-1
        return self.partition(nums, 0, len(nums) - 1, k - 1)

    def partition(self, nums, left, right, k):
        if left >= right:
            return nums[k]
        pivot = left
        prev = left
        for curr in range(left + 1, right + 1):
            if nums[curr] > nums[pivot]:
                continue
            else:
                prev = prev + 1
                nums[prev], nums[curr] = nums[curr], nums[prev]
        nums[prev], nums[pivot] = nums[pivot], nums[prev]

        pivot = prev
        if k < pivot:
            return self.partition(nums, left, pivot - 1, k)
        elif k > pivot:
            return self.partition(nums, pivot + 1, right, k)
        else:
            return nums[k]

sol = Solution()

sol.findKthLargest([9, 3, 2, 4, 8],3)==4

nums = [595240, 373125, 463748, 417209, 209393, 747977, 864346, 419023, 925673, 307640, 597868, 833339, 130763, 814627,
        766415, 79576, 459038, 990103, 944521, 708820, 473246, 499960, 742286, 758503, 270229, 991199, 770718, 529265,
        498975, 721068, 727348, 29619, 712557, 724373, 823743, 318203, 290432, 476213, 412181, 869308, 496482, 793858,
        676162, 165869, 160511, 260864, 502521, 611678, 786798, 356560, 916620, 922168, 89350, 857183, 964051, 979979,
        916565, 186532, 905289, 653307, 351329, 195491, 866281, 183964, 650765, 675046, 661642, 578936, 78684, 50105,
        688326, 648786, 645823, 652329, 961553, 381367, 506439, 77735, 707959, 373271, 316194, 185079, 686945, 342608,
        980794, 78777, 687520, 27772, 711098, 661265, 167824, 688245, 286419, 400823, 198119, 35400, 916784, 81169,
        874377, 377128, 922531, 866135, 319912, 867697, 10904]
sol.findKthLargest(nums,105) == 991199


a = list(sorted(nums))
a[len(a)-105]