# 1218. Longest Arithmetic Subsequence of Given Difference
# Medium
#
# Given an integer array arr and an integer difference, return the length of the longest subsequence in arr
# which is an arithmetic sequence such that the difference between adjacent elements in the subsequence
# equals difference.
#
# A subsequence is a sequence that can be derived from arr by deleting some or no elements without changing
# the order of the remaining elements.
#
# Example 1:
# Input: arr = [1,2,3,4], difference = 1
# Output: 4
# Explanation: The longest arithmetic subsequence is [1,2,3,4].
#
# Example 2:
# Input: arr = [1,3,5,7], difference = 1
# Output: 1
# Explanation: The longest arithmetic subsequence is any single element.
#
# Example 3:
# Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
# Output: 4
# Explanation: The longest arithmetic subsequence is [7,5,3,1].
#
# Constraints:
# 1 <= arr.length <= 105
# -104 <= arr[i], difference <= 104

from typing import List

# 解题思路
# 题目让我们找一个subsequence，使得这个subsequence前一个元素和后一个元素的差值为difference.
# 我们只需要用hashmap就可以了。hashmap当中的key为数字本身，value为连上这个数字之后最长的序列长度。
# 最终遍历一次map我们就可以知道最长的value是多长了。


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        num_to_length = dict()  #  key: number,  value: 连上这个数字之后最长的序列长度。
        rslt =1
        for num in arr:
            if (num - difference) in num_to_length.keys():
                num_to_length[num] = num_to_length[(num - difference)]+1
                rslt = max(rslt, num_to_length[num])
            else:
                num_to_length[num]=1

        return rslt




sol = Solution()
sol.longestSubsequence(arr=[1, 5, 7, 8, 5, 3, 4, 2, 1], difference=-2)
sol.longestSubsequence(arr=[1, 3, 5, 7], difference=1)
sol.longestSubsequence(arr=[1, 2, 3, 4], difference=1)
