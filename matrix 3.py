import numpy as np

# Define the matrix
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

row_sums = np.sum(matrix, axis=1)

column_sums = np.sum(matrix, axis=0)

print("Sum of each row:")
for row_sum in row_sums:
    print(row_sum)

print("\nSum of each column:")
for col_sum in column_sums:
    print(col_sum)
