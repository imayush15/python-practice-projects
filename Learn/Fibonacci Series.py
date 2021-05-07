i=0
first=0
second=1
j = int(input("Enter the range of Fibonacci Series : "))

while i<=j:
    if i<=1:
        next=i
    else:
        next=first+second
        first=second
        second=next
    i+=1

    print(next)

