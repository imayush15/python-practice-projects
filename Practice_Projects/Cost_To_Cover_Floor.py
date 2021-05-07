# This is the program to find the cost of covering the floor
class Area:
    def __init__(self, length, breadth, cost_per_m2):
        self.length = length
        self.breadth = breadth
        self.cost_per_m2 = cost_per_m2

    def total_cost(self):
        area = self.length * self. breadth
        return self.cost_per_m2 *area

length = int(input("Enter the Length of Floor(in Meter) : "))
breadth = int(input("Enter the breadth of Floor(in Meter) :"))
cpc = int(input("Enter the Cost per Sq. Meter For the tile(in ₹) : "))

new_floor = Area(length, breadth, cpc)

result = new_floor.total_cost()

print(f"\nThe Total Cost for covering th whole floor is(in ₹)  : {result}")

