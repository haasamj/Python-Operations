def dec(a,b):
    print(a/b)

def smart_div(func):

    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

dec = smart_div(dec)

dec(2,4)