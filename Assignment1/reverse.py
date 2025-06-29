#to find reverse of two digit number

num=int(input("Enter two digit number"))
a=num//10
b=num%10
reverse=b*10+a
print("Reverse value is the : ",reverse)