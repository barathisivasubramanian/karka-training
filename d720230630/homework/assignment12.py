y=int(input("Enter the year to check whether it is leap year or not"))
if y%4==0 and y%100!=0 or y%400==0:
    print("The given year is a leap year")
else:
    print("Entered year is not a leap year")
 