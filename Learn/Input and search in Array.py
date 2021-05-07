from array import *

arr = array('i', [])

x = int(input("Enter the length of array : "))

for i in range(x):
    y = int(input("Enter next value :"))
    arr.append(y)

print(arr)

z = int(input("Enter the number to get its index number : "))
k = 0
for e in arr:
    if e==z:
        print("Index number is", k)

    k+=1

