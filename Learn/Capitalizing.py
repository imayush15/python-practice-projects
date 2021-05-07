# Write a function that capitalizes the first and fourth letters of a name

def myfunc(mystring):

    first_letter = mystring[0]
    inbetween = mystring[1:3]
    fourth_letter = mystring[3]
    rest = mystring[4:]

    return first_letter.upper() + inbetween + fourth_letter.upper() + rest
result = myfunc("macdonalds")

print(result)


