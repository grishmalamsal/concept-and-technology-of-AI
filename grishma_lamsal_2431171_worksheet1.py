# -*- coding: utf-8 -*-
"""Grishma_lamsal_2431171_worksheet1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1S0gcsGHZm1cO6LISTIODjlWxL-0E4tzF

Problem - 1: Array Creation:

1. Initialize an empty array with size 2X2.
"""

import numpy as np
empty_array = np.empty((2, 2))
print("Empty array :", empty_array)

"""2. Initialize an all one array with size 4X2."""

ones_array = np.ones((4, 2))
print("\n2. All ones array (4x2):\n", ones_array)

"""3. Return a new array of given shape and type, filled with fill value.{Hint: np.full}"""

fill_value = 7
filled_array = np.full((3, 3), fill_value)
print("\n3. Array filled with value 7 (3x3):\n", filled_array)

"""4. Return a new array of zeros with same shape and type as a given array.{Hint: np.zeros like}"""

given_array = np.array([[1, 2, 3], [4, 5, 6]])
zeros_like_array = np.zeros_like(given_array)
print("\n4. Array of zeros with same shape as given array:\n", zeros_like_array)

"""5. Return a new array of ones with same shape and type as a given array.{Hint: np.ones like}"""

ones_like_array = np.ones_like(given_array)
print("\n5. Array of ones with same shape as given array:\n", ones_like_array)

"""6. For an existing list new_list = [1,2,3,4] convert to an numpy array.{Hint: np.array()}"""

new_list = [1, 2, 3, 4]
converted_array = np.array(new_list)
print("\n6. NumPy array from list:\n", converted_array)

"""Problem - 2: Array Manipulation: Numerical Ranges and Array indexing:

1.Create an array with values ranging from 10 to 49. {Hint:np.arrange()}.
"""

array_10_to_49 = np.arange(10, 50)
print("1. Array from 10 to 49:\n", array_10_to_49)

"""2.Create a 3X3 matrix with values ranging from 0 to 8.
{Hint:look for np.reshape()}
"""

matrix_3x3 = np.arange(9).reshape((3, 3))
print("\n2. 3x3 matrix with values 0 to 8:\n", matrix_3x3)

"""3.Create a 3X3 identity matrix.{Hint:np.eye()}"""

identity_matrix = np.eye(3)
print("\n3. 3x3 identity matrix:\n", identity_matrix)

"""4.Create a random array of size 30 and find the mean of the array.
{Hint:check for np.random.random() and array.mean() function}
"""

identity_matrix = np.eye(3)
print("\n3. 3x3 identity matrix:\n", identity_matrix)

"""5.Create a 10X10 array with random values and find the minimum and maximum values."""

random_matrix = np.random.random((10, 10))
min_value = random_matrix.min()
max_value = random_matrix.max()
print("\n5. Random 10x10 array min and max:\nMin:", min_value, "\nMax:", max_value)

"""6.Create a zero array of size 10 and replace 5th element with 1."""

zero_array = np.zeros(10)
zero_array[4] = 1
print("\n6. Zero array with 5th element replaced with 1:\n", zero_array)

"""7.Reverse an array arr = [1,2,0,0,4,0]."""

arr = np.array([1, 2, 0, 0, 4, 0])
reversed_array = arr[::-1]
print("\n7. Reversed array:\n", reversed_array)

"""8.Create a 2d array with 1 on border and 0 inside."""

border_array = np.ones((5, 5))
border_array[1:-1, 1:-1] = 0
print("\n8. 2D array with 1 on border and 0 inside:\n", border_array)

"""9.Create a 8X8 matrix and fill it with a checkerboard pattern."""

checkerboard = np.zeros((8, 8), dtype=int)
checkerboard[1::2, ::2] = 1
checkerboard[::2, 1::2] = 1
print(" Checkerboard pattern (8x8)", checkerboard)

"""Problem - 3: Array Operations:

1. Add the two array.
"""

import numpy as np

x = np.array([[1, 2], [3, 5]])
y = np.array([[5, 6], [7, 8]])
v = np.array([9, 10])
w = np.array([11, 12])


add_xy = x + y
print(" Addition of x and y is :", add_xy)

"""2. Subtract the two array."""

import numpy as np

x = np.array([[1, 2], [3, 5]])
y = np.array([[5, 6], [7, 8]])
v = np.array([9, 10])
w = np.array([11, 12])

array_difference = x - y
print("the Difference of x and y is :", array_difference)

"""3. Multiply the array with any integers of your choice."""

import numpy as np

x = np.array([[1, 2], [3, 5]])
y = np.array([[5, 6], [7, 8]])
v = np.array([9, 10])
w = np.array([11, 12])

mult=x*3
print("multiplication of x by 3 is:",mult)

"""4. Find the square of each element of the array."""

import numpy as np

x = np.array([[1, 2], [3, 5]])
y = np.array([[5, 6], [7, 8]])
v = np.array([9, 10])
w = np.array([11, 12])

square= x**2
print("square of x is:",square)

"""5. Find the dot product between: v(and)w ; x(and)v ; x(and)y."""

import numpy as np

x = np.array([[1, 2], [3, 5]])
y = np.array([[5, 6], [7, 8]])
v = np.array([9, 10])
w = np.array([11, 12])

dot_product_vw = np.dot(v, w)
dot_product_xv = np.dot(x, v)
dot_product_xy = np.dot(x, y)

print("Dot product of v and w:", dot_product_vw)
print("Dot product of x and v:", dot_product_xv)
print("Dot product of x and y:", dot_product_xy)

"""6. Concatenate x(and)y along row and Concatenate v(and)w along column.
{Hint:try np.concatenate() or np.vstack() functions.
"""

import numpy as np

x = np.array([[1, 2], [3, 5]])
y = np.array([[5, 6], [7, 8]])
v = np.array([9, 10])
w = np.array([11, 12])

concat_xy = np.vstack((x, y))
concat_vw = np.column_stack((v, w))


print("Concatenation of x and y along the rows is:", concat_xy)
print("Concatenation of v and w along the columns is:", concat_vw)

"""7. Concatenate x(and)v; if you get an error, observe and explain why did you get the error?"""

try:
    concat_xv = np.concatenate((x, v), axis=0)
    print(" Concatenation of x and v is :", concat_xv)
except ValueError as e:
    print("Error when concatenating x and v is:")
    print(e)
    print("x has a shape of (2, 2), while v has a shape of (2,). For concatenation, dimensions must match. You could reshape `v` to be (1, 2) or expand it to align the dimensions.")

"""Problem - 4: Matrix Operations:

• For the following arrays:
A = np.array([[3,4],[7,8]]) and B = np.array([[5,3],[2,1]]);
Prove following with Numpy:
1. Prove A.A−1 = I.
2. Prove AB ̸= BA.
3. Prove (AB)

T = BTAT
"""

import numpy as np

A=np.array([[3,4],[7,8]])
B=np.array([[5,3],[2,1]])
#1
A_inverse=np.linalg.inv(A)
identity_matrix=np.dot(A,A_inverse)

print(" Prove A.A−1 = I.")
print(identity_matrix)
#2
AB=np.dot(A,B)
BA=np.dot(B,A)
print("Prove AB ̸= BA.")
print(AB)
print(BA)
#3
AB_transpose=np.dot(A,B)
AT_BT=np.dot(B.T,A.T)
print("Prove (AB)T=BTAT")
print(AB_transpose)
print(AT_BT)

"""• Solve the following system of Linear equation using Inverse Methods.

2x − 3y + z = −1
x − y + 2z = −3
3x + y − z = 9

{Hint: First use Numpy array to represent the equation in Matrix form. Then Solve for: AX = B}

"""

A_eq=np.array([[2,-3,1],[1,-1,2],[3,1,-1]])
B_eq=np.array([-1,-3,9])
solution=np.linalg.solve(A_eq,B_eq)
print("The solution is:",solution)

"""• Now: solve the above equation using np.linalg.inv function.{Explore more about ”linalg” function of Numpy}"""

sol=np.linalg.inv(A_eq).dot(B_eq)
print("The solution is:",sol)