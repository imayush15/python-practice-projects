print("ROCK PAPER SCISSOR Game :=")

x = input("Player 1, Enter Your Name : ")
y = input("Player 2, Enter Your Name : ")

print("Use 1 -> Rock, 2 -> Paper, 3 -> Scissor")

p1 = int(input("{}, Enter Your Choice : ".format(x)))

p2 = int(input("{}, Enter Your Choice : ".format(y)))

if p1==1 and p2==2:
    print("{} WINS :)".format(x))
elif p1==1 and p2==3:
    print("{} WINS".format(x))
elif p1==2 and p2==1:
    print("{} WINS".format(y))
elif p1==2 and p2==3:
    print("{} WINS".format(y))
elif p1==3 and p2==1:
    print("{} WINS".format(y))
elif p1==3 and p2==2:
    print("{} WINS".format(x))
else:
    print("INVALID INPUT")
