# write a program to find the area and perimeter of following figure(accept the length breadth and radius from user)

length=int(input("Enter length: "))
breadth=int(input("Enter breadth: "))
radius = float(input("Enter radius: "))
area=length*breadth
perimeter= 2 * (length + breadth)
print(area,perimeter)