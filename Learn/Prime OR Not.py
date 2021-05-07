def prime(i):
    for j in range(2, i):
        if i % j == 0:
            print("Entered Number is Not Prime")
            break

    else:
        print("Entered Number is prime")



i = int(input("Enter a number :"))
prime(i)

