def count(a):
    name = 0
    for i in a:
        if len(i)<=n:
            name += 1
    print(name)

n = int(input("Enter how many elements you want in a list: "))
a = []

for i in range(n):
    b = input("Enter names: ")
    a.append(b)

print(a)
count(a)