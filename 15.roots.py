a =int(input("Enter Coficient of x^2:"))
b=int(input("Enter Coficient of x:"))
c=int(input("Enter a Constant:"))
xe=(-b+(b**2-4*a*c)**0.5)/2*a
ye=(-b-(b**2-4*a*c)**0.5)/2*a
print(f"{a}x^2+({b})x+{c}")
print("Roots are=",xe,",",ye)
