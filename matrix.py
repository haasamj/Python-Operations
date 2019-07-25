from numpy import *

# arr = array([
#     [2,4,5,3],
#     [4,2,1,4],
#     [4,5,9,8]]
# )

# m = matrix('1 2; 3 4;5 6; 7 9') #you can create rows and colums through this ; end of rows and space end of column
# print(m)
# arr1 = arr.flatten()
# arr2 = arr1.reshape(2,3,2) #you can change shape by reshape function in this 2 array in array 3 rows and 2 col.
# print(arr2)
# print(arr.ndim)
# print(arr.dtype)

# print(arr.shape)
# print(arr.size)
# a = matrix('1 2 3;4 5 6;7 8 9')
# b = matrix('2 2 7;9 9 0; 1 3 2')
# print(diagonal(a))
# print(a.min())
# print(a.max())

# c = a * b
# print(a)
# print(b)
# print(c)

arr1 = array([
    [1,2,4],
    [4,2,5]
])

arr2 = array([
    [2,4,2],
    [5,6,6]
])

arr2 = arr2.reshape(3,2)

if arr1.shape[1] == arr2.shape[0]:
    for arr1