def linear_interp(xs, ys, x):
    if len(xs) != len(ys):
        raise Exception("size of xs and ys must match")

    if x <= min(xs):
        return min(xs)
    if x >= max(xs):
        return max(xs)

    a = sorted(zip(xs, ys))
    xs = [item[0] for item in a]
    ys = [item[1] for item in a]

    # find upper bound
    j = 0
    # x_post = xs[j]
    while xs[j] < x:
        j += 1

    i = j - 1

    y_interp = ys[i] + (ys[j] - ys[i]) / (xs[j] - xs[i]) * (x - xs[i])

    return y_interp


xs = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8]
ys = [10, 20, 30, 40, 55, 50, 50, 60, 70, 80]

# xs = [2, 3, 1, -2]
# ys = [20, 30, 14, -21]
sorted(zip(xs, ys))
