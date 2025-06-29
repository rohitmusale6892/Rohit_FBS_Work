num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
num3=int(input("Enter num3: "))
answer=(num2*num2)-(4*num1*num3)    #b squre-4ac
answer=answer **0.5
root1=(-num2+answer)/(2*num1)
root2=(-num2-answer)/(2*num1)
print("Root1",root1)
print("Root2",root2)