from random import *
print("This is a Guess Game : \nComputer will choose any number between 0 to 5 \nand you have to guess what is the number :=")

inp = int(input("Enter any Number Between 0 to 5 : "))

x = randint(0, 5)

if x==inp:
    print("You Guessed the correct Number :)")
else:
    print("Computer Chose", x)
    print("You Were Pretty Close !")

