# 378. Kth Smallest Element in a Sorted Matrix
# Medium
#
# Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.
#
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
#
# Example:
# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
#
# return 13.
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ n2.
#
#

from typing import List
import heapq


# 用堆解决:
# 定义一个小根堆, 起始仅仅放入第一行第一列的元素.
# 循环k次, 每一次取出一个元素, 然后把该元素右方以及下方的元素放入堆中, 第k
# 次取出的元素即为答案.其中,要注意一个元素不能重复入堆, 需要记录.

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # m rows, n columns
        m = len(matrix)
        if m == 0:
            return None
        n = len(matrix[0])
        if n == 0:
            return None

        # a tuple of (matrix element, row number, col number)
        minheap = []
        heapq.heappush(minheap, (matrix[0][0], 0, 0))
        visited = {(0, 0)}
        num = None
        for _ in range(k):
            num, i, j = heapq.heappop(minheap)
            # search for number in the same column but next row
            if i + 1 < m and (i + 1, j) not in visited:
                heapq.heappush(minheap, (matrix[i + 1][j], i + 1, j))
                visited.add((i+1,j))
            # search for number in the same row but next column
            if j+1<n and (i,j+1) not in visited:
                heapq.heappush(minheap,  (matrix[i][j+1], i,j+1))
                visited.add((i,j+1))

        return num

sol = Solution()
assert sol.kthSmallest(matrix=[[1, 5, 7], [3, 7, 8], [4, 8, 9]], k=4) == 5
assert sol.kthSmallest(matrix=[[1], [2], [3], [100], [101], [1000], [9999]], k=5) == 101

