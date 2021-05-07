def pal(str):
    RevStr = ''
    for i in str:
        RevStr = i + RevStr
    print("Entered String is : ", RevStr)
    if str==RevStr:
        print("Entered String is Palindrome :)")
    else:
        print("Sorry! Not a Palindrome :)")



print("A PALINDROME FUNCTION : ")

str = input("Enter a String : ")

pal(str)



