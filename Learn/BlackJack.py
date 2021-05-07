'''
BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
Finally, if the sum (even after adjustment) exceeds 21, return 'BUST
'''


def Jack(mylist):
    j = 0
    for i in mylist:
        j = j + i

    if j <= 21:
        return j
    elif j >= 21 and i == 11:
        j = j - 10
    elif j > 21:
        return "BUST"


list1 = []

k = int(input("Enter the range of list : "))

for x in range(k):
    y = int(input("Enter the Value : "))
    list1.append(y)

result = Jack(list1)

print(result)