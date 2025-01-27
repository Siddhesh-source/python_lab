list1=[43,436,54,5684,4745,7453,4363]
even=[]
odd=[]
for num in list1:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
print(even)
print(odd)
