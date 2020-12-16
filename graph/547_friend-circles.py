# 547. Friend Circles
# Medium
#
# There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature.
# For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C.
# And we defined a friend circle is a group of students who are direct or indirect friends.
#
# Given a N*N matrix M representing the friend relationship between students in the class.
# If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not.
# And you have to output the total number of friend circles among all the students.
#
# Example 1:
# Input:
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
#
# Output: 2
# Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
# The 2nd student himself is in a friend circle. So return 2.
#
#
# Example 2:
# Input:
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
#
# Output: 1
# Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
# so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
#
# Constraints:
# 1 <= N <= 200
# M[i][i] == 1
# M[i][j] == M[j][i]

from typing import List


class Solution:
    # in this problem, friends is define by using adjacent list.
    # this problem is like the number of island, so if we find one people. we recursively visit all of his friend, and
    # his friend's friend.
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        visited = [False for _ in range(n)]
        friend_circles = 0
        for i in range(n):
            if visited[i]:
                continue
            self.dfs_visit_friends(M, total_people=n, current_person=i, visited=visited)
            friend_circles += 1
        return friend_circles

    def dfs_visit_friends(self, M, total_people, current_person, visited):
        visited[current_person] = True
        for i in range(total_people):
            # current person is friend with the ith person and we have not visit the ith person yet
            if M[current_person][i] == 1 and (not visited[i]):
                self.dfs_visit_friends(M, total_people, i, visited)


sol = Solution()
m = [[1, 1, 0],
     [1, 1, 1],
     [0, 1, 1]]

sol.findCircleNum(M=m)
