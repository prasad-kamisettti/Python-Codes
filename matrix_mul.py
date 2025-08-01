matrix_a = [[7, 8], [13, 49]]
matrix_b = [[9, 3], [0, 0]]

result = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        result[i][j] = (matrix_a[i][0] * matrix_b[0][j] +
                        matrix_a[i][1] * matrix_b[1][j])

for row in result:
    print(row)