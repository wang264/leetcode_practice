from collections import deque

# number of island, 8 direction, left right connected.top down is not


# 0 0 0 0 0 1 0 0 1 0 0 0
# 1 0 0 0 0 0 1 0 0 0 0 1
# 0 0 0 0 0 0 0 0 0 0 0 0


# find number of clusters
# left right is a circle
# top down is not a circle
# eight direction.

DELTAS = [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]


def number_of_clusters(matrix):
    # edge cases
    if not matrix or len(matrix) == 0:
        return 0
    visited = set()
    clusters = 0
    rows = len(matrix)
    cols = len(matrix[0])
    for row in range(rows):
        for col in range(cols):
            if (row, col) in visited:
                continue
            if matrix[row][col] == 1:
                clusters += 1
                bfs_helper(matrix, start_row=row, start_col=col, visited=visited)

    return clusters


def bfs_helper(matrix, start_row, start_col, visited):
    number_of_cols = len(matrix[0])
    q = deque([(start_row, start_col)])
    while q:
        for _ in range(len(q)):
            cell = q.popleft()
            row, col = cell
            for d_row, d_col in DELTAS:
                next_row = d_row + row
                next_col = d_col + col

                # mod because left right is connected
                next_col = next_col % number_of_cols

                # if we are out of bound, we visited this cell before,
                if (not is_valid(matrix, next_row, next_col)) or (next_row, next_col) in visited or matrix[next_row][
                    next_col] == 0:
                    continue
                q.append((next_row, next_col))
                visited.add((next_row, next_col))


# it left-right is connected.
def is_valid(matrix, next_row, next_col):
    rows = len(matrix)
    # cols = len(matrix)

    if 0 <= next_row <= rows - 1:
        return True
    else:
        return False


# 0 0 0 0 0 1 0 0 1 0 0 0
# 1 0 0 0 0 0 1 0 0 0 0 1
# 0 0 0 0 0 0 0 0 0 0 0 0

# matrix = [[ 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
#          [  1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
#          [  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# matrix=None

# matrix = [[1,0,1]]
# matrix = [[0,0]]

# matrix =[[0]]

rslt = number_of_clusters(matrix=matrix)
print(rslt)
# assert rslt==3
