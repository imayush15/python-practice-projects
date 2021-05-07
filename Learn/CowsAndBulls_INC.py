#this is a game called cows and bulls

from random import *

i=1
c=0
while i<=4:
    x = randint(1,9)
    c = (c*10)+x
    i+=1

print("\nRandom Number is : ", c)

