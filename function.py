
# def add_sub(x,y):
#     z = x+y
#     z1 = x-y
#     return z,z1
#
#
# result, result1 = add_sub(3,2)
# print(result, result1)

# def update(x):
#     print(id(x))
#     x = 5
#     print(id(x))
#     print(x)
#
# a = 2
# print(id(a))
# update(a)
# print(a)

# def update(lst):
#     print(id(lst))
#     lst[1] = 15
#     print(id(lst))
#     print(lst)
#
# lst = [10,20,25]
# print(id(lst))
# update(lst)
# print(lst)

#Types of argument

# Position
# Keyword
# Default
# Variable Length

# Postion

# def add(a,b):
#     c = a+b
#     return c
#
# a = add(2,5)    #position should be right like a = 2, b = 5
# print(a)

# Keyword

# def person(name,age):
#     print("Name: ",name)
#     print("Age: ",age)
#
# person(age=24,name='navai')

#default argument

# def person(name,age=18):
#     print("name: ",name)
#     print("age: ",age)
#
# person('navin',34)

#variable length

# def add(a,*b):
#     c = a
#     for i in b:
#         c = c+i
#     print(c)   #we are denoting all others numbers to variable length b. 5,6,8,9 in *b in format of tuple like (5,6,8,9)
#
# add(3,5,6,8,9)

#keyword variable length

# def person(name,**other):
#     print(name)
#     for i,j in other.items():
#         print(i,":",j)
#
# person('navin',age=28,gender='male',mobno='9910457528')

# Global Keyword
# a = 2
# print(id(a))
# def ass():                     #assigning local and global variable in same function
#     a = 9
#     print(id(a))
#     x = globals()['a']
#     print(id(x))
#     print(a)
#
#     globals()['a'] = 15
#
# ass()
#
# print("outside",a)

#passing a list to a function

# def oper(lst):
#
#     even = [a for a in lst if a%2==0]
#     odd = [a for a in lst if a%2!=0]
#     print(even)
#     print(odd)
#
# lst = [1,2,3,4,5,6,7,8,9,10]
#
# oper(lst)

# or we can do like this

# def count(lst):
#     even =0
#     odd =0
#     for i in lst:
#         if i%2==0:
#             even+=1
#         else:
#             odd+=1
#     return even,odd
#
# n = int(input("Enter the number of elements you want: "))
# lst = []
#
# for i in range(n):
#     a = int(input("Enter the numbers: "))
#     lst.append(a)
# print(lst)
# even, odd = count(lst)
# print("Even : {} and Odd : {}".format(even,odd))
#fabonacci sequence
def fib(n):
    if n>0:
        a = 0
        b = 1
        if n==1:
            print(a)
        else:
            print(a)
            print(b)
            for i in range(2,n):
                c = a + b
                a = b
                b = c
                # print(c)
                if c<=100:
                    print(c)

    else:
        print("Number is less than 1.")

fib(100)




# this one is different this is testing for isalpha
# def oper(lst):
#     b = [a for a in lst if a.isalpha()]
#     print(b)
#
# lst = ['hello world','hi','hello youtube']
#
# oper(lst)