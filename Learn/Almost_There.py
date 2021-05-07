def myfunc(num):
    if (num > 90 and num <110) or ((num > 190 and num <210)):
        return True
    else:
        return False

x = int(input("Enter any Integer between 0 - 300 : "))

result = myfunc(x)

print(result)