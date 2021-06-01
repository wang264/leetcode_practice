# given an infinite long array of 11111111.....000000, find the index of the first 0


def find_first_zero(arr):
    if arr[0] == 0:
        return 0

    end = 1
    while arr[end] != 0:
        end = end << 1

    start = 0

    while start + 1 < end:
        mid = (start + end) // 2
        if arr[mid] == 1:
            start = mid
        elif arr[mid] == 0:
            end = mid

    if arr[start] == 0:
        return start
    else:
        return end


arr = [1]*1000 + [0]*10000000

find_first_zero(arr=arr)
