name = input("Enter name =")
family = input("Enter family =")
a = float(input("Enter score 1 = "))
b = float(input("Enter score 2 = "))
c = float(input("Enter score 3 = "))

Average = (a + b + c) / 3
if Average >= 17:
    print("Great")

if 12 <= Average < 17:
    print("Normal")

if Average < 12:
    print("Fail")    
