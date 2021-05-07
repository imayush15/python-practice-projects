#This is the Program to get how much change is to be returned
def change(cost, value_of_note):
    if cost<=value_of_note:
        return value_of_note - cost
    else:
        return "Need More Money"

cost = int(input("Enter the Cost(in ₹) : "))
note = int(input("Enter The Value Of note Given(in ₹) : "))
result = change(cost, note)
print (f"Change amount to be returned is(in ₹) : {result}")