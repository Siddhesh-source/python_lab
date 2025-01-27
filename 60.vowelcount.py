str1=str(input("Enter name:"))
a=0
for i in str1:
    if i in 'aeiouAEIOU':
        a=a+1
print(a)
