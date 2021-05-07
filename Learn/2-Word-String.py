# Write a function takes a two-word string and returns True if both words begin with same letter

def myfunc(mystring):
    x = mystring.split(" ")
    if x[0][0] == x[1][0]:
        return True
    else :
        return False

a = myfunc("Hello Harry")

print(a)