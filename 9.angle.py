hour=int(input("Enter Hour:"))
min=int(input("Enter min:"))
sec =int(input("Enter sec:"))
angle=hour*30+min*0.5+(sec/120)
print("Angle=",angle)
