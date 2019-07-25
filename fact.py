# def fact(n):
#     a = 1
#     for i in range(1,n+1):
#         a = a*i
#     return a
#
# x = int(input("Enter number for factorial: "))
# result = fact(x)
# print(result)

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

x = int(input("Enter number for factorial: "))
result = fact(x)
print(result)