def dup(x):
    print(list(set(x)))

l = []

z = int(input("Enter the Range : "))

for i in range(z):
    y = input("Enter the Value : ")
    l.append(y)

dup(l)
