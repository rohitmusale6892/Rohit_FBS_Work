# sum of three digit

num=int(input("Enter number"))
a=num%10
num//=10
b=num%10
num//=10
c=num%10
sum=a+b+c
print("Sum",sum)