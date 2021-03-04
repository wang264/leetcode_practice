# We are given a list (sticking with the Python tongue cause I cannot stop loving it!) of positive integers and we have
# to find the maximum even sum for K elements from the list. If we can’t find one, we return -1.
# Notice the emphasis on the word even.
# Sample I/O:
# Input:
# [4, 2, 6, 7, 8], k = 3
# Output:
# 18
# Explanation:
# Since k = 3, we have to take 3 elements from this list. Don’t forget we have to make it an even sum. So, even if the
# sum of [8,7,6] = 21 is the max sum we can get but we can’t take it since it’s an odd number. So, the maximum even
# sum would be the sum of [8,6,4] = 18, which is the maximum even sum we can get.
# Let’s try a couple of more:
# Input:
# [5,5,1,1,3], k = 3
# Output:
# -1
# Explanation:
# Take a look here, we need 3 elements to make the maximum even sum. But notice we don’t have any even number at all.
# Also, it’s impossible that 3 odd numbers will ever add up to an even sum. Consider: 1 + 3 + 5 = 9, so it’s always
# an odd sum. So, we just return -1.


class Solution:
    def largest_even_sum(self, A: list, k: int):
        res = [-1]
        curr_path = []
        curr_sum = 0
        start_idx = 0
        self.dfs_helper(A, start_idx, curr_path, curr_sum, k, res)

        return res[0]

    def dfs_helper(self, A, start_idx, curr_path, curr_sum, k, res):
        if k == 0 and curr_sum % 2 == 0:
            res[0] = max(res[0], curr_sum)
            return
        for i in range(start_idx, len(A)):
            curr_path.append(A[i])
            curr_sum += A[i]
            self.dfs_helper(A, i + 1, curr_path, curr_sum, k - 1, res)
            curr_sum -= A[i]
            curr_path.pop()


sol = Solution()
sol.largest_even_sum(A=[4, 2, 6, 7, 8], k=3)
sol.largest_even_sum(A=[5, 5, 1, 1, 3], k=3)
