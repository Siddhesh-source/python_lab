day=int(input("Enter  Date of Month:"))
month=int(input("Enter Month of Year :"))
year = int(input("Enter a year:"))
if month in[1,3,5,7,8,10,12]:
    if day <=31:
        print("It is Valid date")
    else:
        print("It is Invalid Date")        
elif month in[4,6,9,11]:
    if day <=30:
        print("It is Valid Date")
    else:
        print("It is Invalid Date")
elif month ==2:
    if year %4==0:
        if year%100==0:
            if year %400==0:
                if day <=29:
                    print("It is Valid Date")
                else:
                    print("It is Invalid Date")
            elif day <=28:
                print("It is Valid Date")
            else:
                print("It is Invalid date")
    elif day <=29:
        print("It is Valid date")
    else:
        print("It is Invalid date")
