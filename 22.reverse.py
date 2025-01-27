num=int(input("Enter a Number :"))
c=0
while num>0:
    b =num %10
    c=(c*10)+b
    num=num//10
    
print(c)

