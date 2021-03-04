def josephus(n, k):
    array = list(range(n))
    idx_to_kill = k - 1
    rslt = []
    while len(array) > 1:
        rslt.append(array.pop(idx_to_kill))
        idx_to_kill = (idx_to_kill - 1 + k) % len(array)

    return rslt + array


josephus(10, 3)
