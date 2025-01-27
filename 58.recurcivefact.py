fac=1
def fact(numb):
    if numb==0 or numb==1:
        return 1
    else:
        return fact(numb-1)*numb
num=int(input("enter a number:"))
print(fact(num))
