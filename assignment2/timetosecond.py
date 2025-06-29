# Convert the time entered in hh,min and sec into second

hours=int(input("Enter Hours: "))
min=int(input("Enter Min: "))
sec=int(input("Enter Sec: "))

total=hours*3600+ min*60+ sec
#totalsec=total
print("Total second : ",total)