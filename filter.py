from functools import reduce #It is used for reduce method.

a = [1,4,6,7,9,2]

evens = list(filter(lambda n: n%2==0, a)) #filter function used to filter elements like in this function. We filter for even numbers

print(evens)

double = list(map(lambda n:n*2,evens)) #map function is used for modified values

print(double)

sum = reduce(lambda a,b:a+b,double) #It add all the values of sequence, reduce it is used to reduce the chunks of values

print(sum)
