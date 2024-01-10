from matrix_operations import generate_matrix
from matrix_operations import matrix_operations


qur1 = generate_matrix([2, -3, -4, 2], 2, 2)
qur2 = generate_matrix([-1, -5, 3, -2], 2, 2)

diff = matrix_operations(qur1, qur2, 'subtract')
print(diff)


#q2
it1 = generate_matrix([2, 1, 5, -3], 2, 2)
it2 = generate_matrix([-2, 4, 3, -2], 2, 2)


firs = matrix_operations(it1, it1, 'add')

print("result")
resu = matrix_operations(firs, it2, 'add')
print(resu)

#q3

q3_1 = generate_matrix([2, -3, -4, 2], 2, 2)
q3_2 = generate_matrix([-1, -5, 3, -2], 2, 2)
q3 = matrix_operations(q3_1, q3_2, 'add')
print("q3")
print(q3)



#q5

q5_1 = generate_matrix([-3, 1, -2, 4, 5, -1], 3, 2)
q5_2 = generate_matrix([4, -3, 0, -2, -2, 4], 3, 2)
print("q5")
print(q5_1)
print(q5_2)