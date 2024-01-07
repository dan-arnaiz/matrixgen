import numpy as np

def generate_matrix(array, rows, cols):
    # Check if the array length is equal to rows*cols
    if rows * cols != len(array):
        raise ValueError("Array length must be equal to rows*cols")
    
    # Reshape the array into a matrix
    matrix = np.reshape(array, (rows, cols))
    
    return matrix

def matrix_operations(matrix1, matrix2, operation):
    if operation == 'add':
        result = np.add(matrix1, matrix2)
    elif operation == 'subtract':
        result = np.subtract(matrix1, matrix2)
    elif operation == 'multiply':
        result = np.dot(matrix1, matrix2)
    elif operation == 'divide':
        result = np.divide(matrix1, matrix2)
    else:
        raise ValueError("Error")
    
    return result