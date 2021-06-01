# write a program that, give an integer N. sum all the whole numbers from 1 through N(both inclusive) do not include
# in your sum and of the intermediate value(1 and N inclusive) that are divisible by 5 or 7.


def sum_1_to_n_divided_by_x(n, x):
    b = n // x
    return (1 + b) * b / 2 * x


def add_num_series_ii(n):
    rslt = sum_1_to_n_divided_by_x(n, 1) \
           - sum_1_to_n_divided_by_x(n, 5) - sum_1_to_n_divided_by_x(n, 7) + sum_1_to_n_divided_by_x(n, 5 * 7)

    return int(rslt)


add_num_series_ii(27)
add_num_series_ii(19)
add_num_series_ii(7)
