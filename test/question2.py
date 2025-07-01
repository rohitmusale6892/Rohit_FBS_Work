# Write a program to calculate simple interest based on principle rate and time

principle=int(input("Enter the principle: "))
rate=int(input("Enter rate: "))
time=int(input("Enter year"))
simpleinterest=principle*time*rate/100
print(simpleinterest)