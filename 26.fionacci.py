num = int(input("Enter the Number of Fibonacci Numbers you want:"))
sum = 1
a=1
for i in range(0,num+1):
    print(sum,end=", ")
    sum,a=a,a+sum