a = 'abcd'

a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items

print(a[::-1])
print(a[1::-1])
print(a[:-3:-1])
print(a[-3::-1])

a[::-1]    # all items in the string, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed

#it is based on slice(start, stop, step)

# a[start:stop:step]
#a[slice(start, stop, step)]
