#Final problem for the exception and error handling
def square(num1):
    print(f"Square of {num1} is {num1**2}")

while True:
    try:
        x = int(input("Please Provide any number : "))
        square(x)

    except:
        print("Please Try Again ! :(")
        continue
    else:
        print("Well Done !")
        break