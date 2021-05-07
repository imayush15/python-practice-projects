#Program to Reverse a Sentence

str = input("Enter a String : ")

y = str.split(' ')

length = len(y)

for i in range(length-1, -1, -1):
    print(y[i], end=" ")