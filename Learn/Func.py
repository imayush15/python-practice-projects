'''
Given two integers, return True if the sum of the integers is 20 or
if one of the integers is 20. If not, return False
'''

def myfunc(a, b):
    if a+b==20:
        return True
    elif a == 20 or b == 20:
        return True
    else:
        return False

result = myfunc(15, 5)

print(result)