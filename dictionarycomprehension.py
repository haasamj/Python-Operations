# cube = {i:i**3 for i in range(1,11)}
#
# print(cube)
#
# for i,j in cube.items():
#     print(f"{i}:{j}")

# name = "mahendar"
#
# count_word = {i:name.count(i) for i in name}
#
# print(count_word)

numbers = [1,3,5,2,5,2]

# count_numbers = {i:numbers.count(i) for i in numbers}
#
# print(count_numbers)

count_numbers = {}

for i in numbers:
    count_numbers[i] = numbers.count(i)
    # print(i)

print(count_numbers)
