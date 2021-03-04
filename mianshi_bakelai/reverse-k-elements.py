class Solution:
    def reverse_k(self, A, k):
        start = 0
        end = 0 + k - 1

        while end < len(A):
            self.reverse(A, start, end)
            start += k
            end += k

    def reverse(self, A, start, end):
        while start < end:
            A[start], A[end] = A[end], A[start]
            start += 1
            end -= 1


A = [1, 2, 3, 4, 5]
k = 2
sol = Solution()
sol.reverse_k(A=A,k=2)
print(A)
