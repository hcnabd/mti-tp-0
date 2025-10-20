matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]

result_matrix = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        result_matrix[i][j] = matrix_a[i][j] + matrix_b[i][j]

print(result_matrix)
