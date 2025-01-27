year = int(input('Enter a Year :'))
if year%400==0:
    print("It is leap year")
elif year%100!=0 and year%4==0:
    print("It is Leap year")
else:
    print("it is not Leap Year")
