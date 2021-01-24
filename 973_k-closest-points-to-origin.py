import heapq

from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        max_heap = []
        for x, y in points:
            dist = x * x + y * y
            heapq.heappush(max_heap, (-1 * dist, [x, y]))
            if len(max_heap) > K:
                heapq.heappop(max_heap)

        return [item[1] for item in max_heap]


sol = Solution()
sol.kClosest([[-5, 4], [-6, -5], [4, 6]], 2)
