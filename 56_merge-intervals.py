# 56. Merge Intervals
# Medium

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
#
# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#
# Constraints:
# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        events = []
        for interval in intervals:
            # +1 for enter,  -1 for exit
            events.append((interval[0], "ENTER"))
            events.append((interval[1], "EXIT"))

        events.sort()

        prev_counter = 0
        counter = 0
        rslt = []

        for i, event in enumerate(events):
            if events[i][1] == "ENTER":
                prev_counter = counter
                counter += 1
            else:
                prev_counter = counter
                counter -= 1

            if prev_counter == 0 and counter == 1:
                rslt.append([event[0], None])
            elif prev_counter == 1 and counter == 0:
                rslt[-1][1] = event[0]

        return rslt


sol = Solution()
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals = [[1, 4], [4, 5]]
sol.merge(intervals)
