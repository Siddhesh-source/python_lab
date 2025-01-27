c=0
def sum_dig(num,c):
    if num<=0:
        return
    b=num%10
    c=c+b
    num//=10
    print(c)
    sum_dig(num,c)
num=int(input("enter a number:"))
sum_dig(num,c)
