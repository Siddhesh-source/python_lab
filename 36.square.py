a=[36,37]

for i in a:
    b=0
    c=0
    if (i**0.5)%1==0:
        print(i,"is Perfect Square")
    else:
        print(i,"is not Perfect Square")
    while i >0:
        b =i %10
        c=c+b
        i//=10
    print("The total Sum of Digits is",c)

