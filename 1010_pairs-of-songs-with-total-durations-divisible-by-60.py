# 1010. Pairs of Songs With Total Durations Divisible by 60
# Medium
# Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want
# the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0
#
#
# Example 1:
#
# Input: time = [30,20,150,100,40]
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60
# Example 2:
#
# Input: time = [60,60,60]
# Output: 3
# Explanation: All three pairs have a total duration of 120, which is divisible by 60.
# You are given a list of songs where the ith song has a duration of time[i] seconds.
#
# Constraints:
#
# 1 <= time.length <= 6 * 104
# 1 <= time[i] <= 500
#\

from typing import List

# 按照题意，每个数其实等价于它自身 mod 60的结果，所以可以用一个下标从0 - 59 的数组记录一下对应的原始数字的个数。
# record[ time[i] % 60 ] += 1。
# 然后线性扫描， 对于time里的每个数字，在运算前先把自己这一次减掉: record[temp] -= 1， 这是为了避免重复以及满足题目条件
# j > i。然后再加上需要的数字（60 - temp）的个数。 一个特殊情况是，如果temp = 0， 因为余数不会出现60的情况，
# 无法按上一行的算法进行计算，比如[60, 60, 60]， 但根据中学数学排列组合的思想不难得知， 如果有N个这样的数，
# 那么它们之间任意地取两个共有C N 2 = N * (N - 1) /2 种取法，所以一次计算就可以处理所有的该种情况的数字，

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        record = [0 for _ in range(60)]
        for idx, item in enumerate(time):
            record[item%60]+=1

        rslt = 0
        for i in range(0,len(time)):
            temp = time[i]%60

            if temp!=0:
                record[temp] -=1
                rslt += record[60-temp]
            elif temp==0 and record[0]>1:
                # special case [60,180,60,240]
                rslt += record[0] * (record[0] - 1) // 2
                record[0] = 0

        return rslt
