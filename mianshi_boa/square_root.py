class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        mid = (left + right) / 2
        while abs(x - mid * mid) > 1e-4:
            mid = (left + right) / 2
            if mid * mid < x:
                left = mid
            elif mid * mid > x:
                right = mid
            else:
                return mid

        return mid


sol = Solution()
sol.mySqrt(x=8)


# to find square root of n, let f(x) = x*x - n, to find the root of this. we can use newton algorithm.
# f'(x) = 2*x  f''(x) = 2
# starting point x_0.   x_i+1 = x_n - f(x_n)/f'(x_n)

class Solution2:
    def mySqrt(self, n: int, x_0, max_iter=40) -> int:
        iteration = 0
        x_n = x_0
        while abs(x_n * x_n - n) > 1e-8 and iteration < max_iter:
            f = x_n * x_n - n
            f_prime = 2 * x_n
            x_n = x_n - f / f_prime

        return x_n


sol = Solution2()
sol.mySqrt(n=8, x_0=2)
