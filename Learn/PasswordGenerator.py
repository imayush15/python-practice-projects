from random import *

s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()"

passlen = int(input("Enter the length of password : "))

p = "".join(sample(s, passlen))

print("\nYour Password is : ", p)