def CI(P, R, T):
    i=1
    while i<=T:
        result = (P*R*1)/100
        P = P + result
        i+=1

    print("CI = ", P)

print("Here is a program to find out the COMPOUND INTEREST :-\n")

P = float(input("Enter the Starting amount : ₹"))
R = float(input("Enter Rate : "))
T = int(input("Enter time in Year : "))

CI(P, R, T)

