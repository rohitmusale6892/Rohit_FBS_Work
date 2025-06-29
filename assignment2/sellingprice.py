#WAP to calculate selling price of book based on cost price and discount
cost=int(input("Enter cost of book"))
discount=int(input("Enter discount"))
discountPersent=(discount/100)*cost
sellingprice=cost-discountPersent
print("Selling Price of Books",sellingprice)