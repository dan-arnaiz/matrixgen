import numpy as np

def generate_matrix(array, rows, cols):
    # Check if the array length is equal to rows*cols
    if rows * cols != len(array):
        raise ValueError("Array length must be equal to rows*cols")
    
    # Reshape the array into a matrix
    matrix = np.reshape(array, (rows, cols))
    
    return matrix

array = [1, 2, 3, 4, 5, 6]
matrix = generate_matrix(array, 2, 3)
print(matrix)