from numpy import *

arr = array([3,5,2,8,9])

# arr1 = arr.view() # shallow copy - it is connected also try to change, change effected in both arrays.
arr1 = arr.copy() # deep copy - it is absolute copy of array.
arr[2] = 1

print(arr)
print(arr1)

print(id(arr))
print(id(arr1))