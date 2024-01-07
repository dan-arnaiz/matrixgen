from matrix_operations import generate_matrix
from matrix_operations import matrix_operations

# Dan Floyd L. Arnaiz
# Kent Clyde M. Monteza
# Linear Algebra A123

# Examples

array = [1, 2, 3, 4, 5, 6]
matrix = generate_matrix(array, 2, 3)
print(matrix)

matrix1 = generate_matrix([1, 2, 3, 4], 2, 2)
matrix2 = generate_matrix([5, 6, 7, 8], 2, 2)
result = matrix_operations(matrix1, matrix2, 'add')
print(result)
