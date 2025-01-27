a = int(input("Enter a Number :"))
b = int(input("Enter a Number :"))
c = int(input("Enter a Number :"))
if a>b and a>c:
    print("Biggest Number is",a)
elif b>c:
    print("Biggest Number is",b)
elif a == b == c:
    print("All Numbers are same")
else:
    print("Biggest Number is",c)
