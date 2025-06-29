days=int(input("Enter the number of days: "))
years=days//365
days=days%365
weeks=days//7
days=days%7
print("year:",years,"weeks",weeks,"Days",days)