#WAP to calculate total salary of employee based on basic, da=10% of basic,
#ta=12% of basic, hra=15% of basic.

salary=int(input("Enter salary"))
da=10       #int(input("Enter da: "))
ta=12       #int(input("Enter ta: "))
hra=15      #int(input("Enter hra: "))
#gross=da+ta+hra
da=(da/100)*salary
ta=(ta/100)*salary
hra=(hra/100)*salary
total_salary=salary+da+ta+hra
print("Total salary: ",total_salary)