from matrix_operations import generate_matrix
from matrix_operations import matrix_operations

# MATH022 M2 PART 1 TEST CASE

# TEST CASES
# 1. Generate the Matrices.

# a = generate_matrix([5, 1, 2, 1, 3, 7, 2, 7, 8], 3, 3)
# print("a =")
# print(a)

# b = generate_matrix([-1, 2, -4, 5], 4, 1)
# print("b =")
# print(b)

# c = generate_matrix([0, 0, 0, 0, 0, 0], 3, 2)
# print("c =")
# print(c)

# d = generate_matrix([2, 1, 3, 6, 7], 1, 5)
# print("d =")
# print(d)


# 2. Performing the Operations.
# Item no. 1
item_1A = generate_matrix([2, 1, 3, 3, -2, 1, -1, 0 ,1], 3, 3)
item_1B  = generate_matrix([1, -2, 2, 1, 4, -2], 3, 2)
item1 = matrix_operations(item_1A, item_1B, 'add')
print("Item 1")
print(item1)

# # Item no. 2
# x = generate_matrix([2, 1, 3], 1, 3)
# y = generate_matrix([-2, 1, -3], 3, 1)
# item2 = matrix_operations(x, y, 'multiply')
# print("Item 2")
# print(item2)

# # Item no. 3
# F = generate_matrix([2, -1, 3, 0 ,-5, 2], 3, 2)
# H = generate_matrix([1, 6, -1, -2, 0, -3], 3, 2)
# item3 = matrix_operations(F, H, 'add')
# print("Item 3")
# print(item3)

# # Item no. 4
# item_4C = generate_matrix([3, -1, -2, 2], 2, 2)
# item_4A  = generate_matrix([2, 0, 1, 4], 2, 2)
# item4 = matrix_operations(item_4C, item_4A, 'subtract')
# print("Item 4")
# print(item4)

# # Item no. 5
# item_5A = generate_matrix([1, 0, -3, -2, 4, 1], 2, 3)
# item_5B = generate_matrix([1, 0, 4, 1, -2, 3, -1, 5, 0, -1, 2, 1], 3, 4)
# item5 = matrix_operations(item_5A, item_5B, 'multiply')
# print("Item 5")
# print(item5)

# # Item no. 6
# item_6C = generate_matrix([1, -2, 0, 4, -3, 1], 3, 2)
# item_6D = generate_matrix([2, -1, 3, 0], 2, 2)
# item6 = matrix_operations(item_6D, item_6C, 'multiply')
# print("Item 6")
# print(item6)