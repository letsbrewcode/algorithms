def make_zero_matrix(matrix):
    L = len(matrix)
    B = len(matrix[0])
    rows = []
    cols = []

    for row in range(L):
        for col in range(B):
            if matrix[row][col] == 0:
                rows.append(row)
                cols.append(col)

    for row in rows:
        for col in range(B):
            matrix[row][col] = 0

    for col in cols:
        for row in range(L):
            matrix[row][col] = 0

    return matrix

if __name__ == '__main__':
    m1 = [[1, 1, 1],
          [1, 0, 1],
          [1, 1, 1]]

    m2 = [[1, 0, 0],
          [1, 1, 1],
          [1, 1, 0]]

    m3 = [[1, 0],
          [0, 1]]

    tests = [m1, m2, m3]
    
    for t in tests:
        result = make_zero_matrix(t)
