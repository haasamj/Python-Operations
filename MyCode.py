def reverse(n):
    m = n[::-1]
    if n==m:
        print('It is palindrome')
    else:
        print('It is not palindrome')
    isValue()

def getValue():
    a = input("Enter a string which is palindrome: ")
    reverse(a)

def isValue():
    a = input("Do you want to check more string which is palindrome or not it is: ")
    if a=="y":
        getValue()
    else:
        print("Thanks for using our software.")

isValue()