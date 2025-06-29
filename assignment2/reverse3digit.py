# Reverse value for three digit number

num=int(input("Enter number"))
a=num%10
num//=10
b=num%10
#num//=10
c=num//10
reverse=(a*10)+b
reverse=(reverse*10)+c
print("Reverse value is: ",reverse)