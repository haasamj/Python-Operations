nums = [1,2,3,4,5,6,7,8,9]

# my_list = []
#
# for n in nums:
#     my_list.append(n)
## my_list = [n for n in nums]

# my_list = [n*n for n in nums]
#
# print(my_list)

my_list = [(letter, num) for letter in 'abcd' for num in range(0,4)]

print(my_list)
