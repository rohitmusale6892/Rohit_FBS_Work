#calculate the cost of painting the following building walls you need to accept area and cost of both interior and exterior wall

height=int(input("Enter the height"))
width=int(input("Enter the width"))
length=int(input("Enter the length"))
area=length*height*width
cost=2*area
print(area)
print(cost)