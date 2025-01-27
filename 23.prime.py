num=int(input("Enter a Number :"))
if num<2:
    print("It is A Prime")
else:
    for a in range(2,num):
        if num%a==0:
            print("it is a not prime")
            break
    else:
        print("It a Prime")