# ****
# ***
# **
# *

# i = 1
# k = 4
# while i<=4:
#     j = 1
#     while j<=k:
#         print("*",end="")
#         j += 1
#     k -= 1
#     i += 1
#     print()

for i in range(4):
    for j in range(4 - i):
        print("#", end="")
    print()

# ****
# ****
# ****
# ****

# i = 1
#
# while i<=4:
#     j = 1
#     while j<=4:
#         print("*",end="")
#         j += 1
#     i += 1
#     print()

# for i in range(4):
#     for j in range(4):
#         print("#",end="")
#     print()

# *
# **
# ***
# ****
#
# i = 1
# k = 1
# while i<=4:
#     j = 1
#     while j<=k:
#         print("*",end="")
#         j += 1
#     i+=1
#     k+=1
#     print()

# for i in range(4):
#     for j in range(i+1):
#         print("#", end="")
#     print()
