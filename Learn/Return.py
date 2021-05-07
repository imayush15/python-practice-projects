'''
Write a function that returns the lesser of two given numbers if both numbers are even,
but returns the greater if one or both numbers are odd
'''

def myfunc(x, y):
    if x%2==0 and y%2==0:
        if x<y:
            return x
        else:
            return y
    elif x%2==1 or y%2==1:
        if x>y:
            return x
        else:
            return y

a = myfunc(2, 7)

print(a)
