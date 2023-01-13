a = float(input("Enter a ="))
b = float(input("Enter b ="))
c = float(input("Enter c ="))

if a < b + c and b < a + c and c < a + b :
    print("True")
else :
    print("False")   
