# 4. Median of Two Sorted Arrays
# Hard

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
# Follow up: The overall run time complexity should be O(log (m+n)).
#
# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
#
# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
#
# Example 3:
# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000
#
# Example 4:
# Input: nums1 = [], nums2 = [1]
# Output: 1.00000
#
# Example 5:
# Input: nums1 = [2], nums2 = []
# Output: 2.00000
#
# Constraints:
#
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106


from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        size_a = len(nums1)
        size_b = len(nums2)
        n = size_a + size_b
        # if n is odd, then this is the index of media
        # if n is even, then the index is biaas towards the right, need to average with th number to its left to
        # get the true median

        if n % 2 == 0:
            return (self.find_kth(nums1, nums2, n // 2+1) + self.find_kth(nums1, nums2, n // 2)) / 2.0
        else:
            return self.find_kth(nums1, nums2, n // 2 + 1)

    # find the Kth largest number in the two sorted array, A and B
    def find_kth(self, A, B, k):
        if len(A) == 0:
            return B[k - 1]
        if len(B) == 0:
            return A[k - 1]

        # possible kth largest number
        start = min(A[0],B[0])
        end = max(A[-1],B[-1])

        while start+1<end:
            mid = (start+end)//2
            # if together there are less than k element smaller or equal to the mid value.
            # we need to look for larger value
            if self.count_smaller_or_equal(A,mid)+self.count_smaller_or_equal(B,mid)<k:
                start = mid
            else:
                end = mid

        if self.count_smaller_or_equal(A,start)+self.count_smaller_or_equal(B,start)>=k:
            return start
        return end

    # count the number of element in array A that are smaller or equal to the target
    def count_smaller_or_equal(self, A,target):
        n = len(A)
        left = 0
        right = n-1
        while left+1<right:
            mid = (left+right)//2
            if A[mid]<=target:
                left = mid
            else:
                right = mid

        # if left=4, then if A[4](the fifth) element is smaller that target
        # which means there are 4 elements smaller or equal to target
        if A[left] > target:
            return left
        if A[right] > target:
            return right

        return len(A)


sol = Solution()
assert sol.findMedianSortedArrays(nums1=[1, 2, 3, 4, 5, 6], nums2=[2, 3, 4, 5]) == 3.5
assert sol.findMedianSortedArrays(nums1=[], nums2=[1]) == 1
assert sol.findMedianSortedArrays(nums1=[5, 6, 9, 10], nums2=[0, 2, 3, 4])==4.5
