list1=[234,564,86,4,679,3,45,46,43,64,45,23,324,23]
for i in range(0,len(list1)):
    for j in range(i+1,len(list1)):
        if j==len(list1):
            break
        elif list1[i]==list1[j]:
            list1.remove(list1[j])
print(list1)
