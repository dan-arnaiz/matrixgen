from matrix_operations import generate_matrix
from matrix_operations import matrix_operations

array = [1, 2, 3, 4, 5, 6]
matrix42 = generate_matrix(array, 2, 3)
print(matrix42)

matrix1 = generate_matrix([1, 2, 3, 4], 2, 2)
matrix2 = generate_matrix([5, 6, 7, 8], 2, 2)

result = matrix_operations(matrix1, matrix2, 'add')
print(result)

b = generate_matrix([-1, 2, -4, 5], 4, 1)
print("b =")
print(b)