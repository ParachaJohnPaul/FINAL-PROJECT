matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9] ]


transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


print("Original 3x3 matrix:")
for row in matrix:
    print(row)


print("Transposed 3x3 matrix:")
for row in transposed_matrix:
    print(row)
