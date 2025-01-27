num=int(input("Enter a Number:"))
c=0
while num>0:
    b =num %10
    c=c+b
    num//=10
print(c)
