def fact(n):
    f=1
    for i in range(1, n+1):
        f = f * i

    return f

x = int(input("Enter the number to get its factorial : "))
result = fact(x)

print("Factorial of {} is {}".format(x, result))
