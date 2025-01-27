tup=()
num=int(input("How man Numbers You want to Add:"))
for a in range(0,num):
    b=int(input("Enter a Element:"))
    temp=list(tup)
    temp.append(b) # type: ignore
    tup=tuple(temp)
print(tup)
