from array import *

print("This is the program to inpurt and find the largest element of an array :- ")

arr = array('i',[])

x = int(input("Enter the length of Array : "))

for i in range(x):
    y = int(input("Enter the Next Value : "))
    arr.append(y)

print(arr)

print("Largest Element of the array is", max(arr))