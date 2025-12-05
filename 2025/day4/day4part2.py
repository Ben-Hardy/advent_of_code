import numpy as np

def count_rolls(mat, row, col):
    if mat[row, col] == 0:
        return -1

    if row == 0:
        dims_row = [row, row + 2]
    elif row + 1 == mat.shape[0]:
        dims_row = [row - 1, row + 1]
    else:
        dims_row = [row - 1, row + 2]

    if col == 0:
        dims_col = [col, col + 2]
    elif col + 1 == mat.shape[1]:
        dims_col = [col - 1, col + 1]
    else:
        dims_col = [col - 1, col + 2]

    # chop out a chunk of the matrix and add it up. -1 because we don't count the middle roll
    return mat[dims_row[0]:dims_row[1], dims_col[0]:dims_col[1]].sum() - 1


with open("input/input.txt") as f:
    lines = f.read().split("\n")

    chunks = []
    for line in lines:
        conv = [1 if i == '@' else 0 for i in line]
        chunks.append(conv)
    m = np.array(chunks)

    still_emptying = True
    total = 0
    while still_emptying:
        cur_total = 0
        to_remove = []
        for i in range(m.shape[0]):
            for j in range(m.shape[1]):
                if 0 <= count_rolls(m, i, j) <= 3:
                    cur_total += 1
                    to_remove.append([i,j])

        total += cur_total
        for item in to_remove:
            m[item[0], item[1]] = 0
        if cur_total == 0:
            still_emptying = False
    print(total)