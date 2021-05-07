def myfunc(mystring):

    wordlist = mystring.split()

    reversed_list = wordlist[::-1]

    return " ".join(reversed_list)
x = input("Enter a Sentence : ")

result = myfunc(x)

print("The Reversed Sentence is : ", result)
