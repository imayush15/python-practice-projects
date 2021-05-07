#Class
class Account():
    def __init__(self, owner, balance = 100):

        # Expecting a String
        self.owner = owner

        # Expecting an Integer
        self.balance = balance

    def deposit(self, dep):

        self.dep = dep
        self.balance = self.balance + dep
        return f"Deposit Accepted, Total Balance : {self.balance} Rupees"

    def withdraw(self):
        h = int(input("\nDo You Wish To Withdraw Money :- \nFor 'YES' Press 1 and For 'No' Press 2 : "))
        if h==1:
            w = int(input("\nEnter the amount to be Withdrwan : "))
            if w>self.balance:
                print("\nInsufficient Account Balance")
            else:
                left = self.balance - w
                print(f"Amount Withdrawn : {w}\nLatest Balance : {left}")
        else:
            print("\nThanks For The Visit, Have a nice Day :)")

    def __str__(self):
        return f"Account Owner : {self.owner} \nAccount Balance : {self.balance} "

print("WELCOME to PyBank, Follow The Steps to Get Your First PyBank Account :\n\n")

name = str(input("Enter Name : "))
sum_ammount = int(input("Enter the Ammount You wish to deposit Now : "))

newacc = Account(name, sum_ammount)

print(f"\nCongratulations, Your New Account has been created ! \n\nHere are the following details : \n{newacc}")

decision = str.upper(input("\nEnter Yes/No\n\nDo You Wish To Deposit Now : "))

if decision =='YES':
    inp = int(input("Enter the amount to be deposited : "))
    b = newacc.deposit(inp)
    print(b)
else:
        c =newacc.withdraw()
        print(c)
