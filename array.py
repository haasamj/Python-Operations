# from array import *
#
# vals = array('i',[5,9,-8,4,2])
#
# newArray = array(vals.typecode,(a*a for a in vals))
#
# # for i in range(len(vals)):
# #     print(vals[i])
#
# for i in newArray:
#     print(i)

from array import *

arr = array('i',[])

n = int(input("Enter how many elements you want in array: "))

for i in range(n):
    x = int(input("Enter the next value: "))
    arr.append(x)

for i in arr:
    print(i)

val = int(input("Enter the value for search: "))

k = 0
for e in arr:
    if e==val:
        print("Your search index number is: ",k)
        break
    k += 1

print(arr.index(val))
