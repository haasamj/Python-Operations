a = "Singhal121997@gmail.com"

result = ''

for i in a:

    if ord(i)>=65 and ord(i)<=90:
        result += chr(ord(i) + 32)
    else:
        result += chr(ord(i))

print(result)
