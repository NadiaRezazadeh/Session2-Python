import math

op = input("enter op =")

if op == "+":
        a = float(input("enter a ="))
        b = float(input("enter b ="))
        result = a + b

if op == "-":
        a = float(input("enter a ="))    
        b = float(input("enter b ="))  
        result = a - b

if op == "*":
        a = float(input("enter a ="))    
        b = float(input("enter b ="))  
        result = a * b
          
if op == "/":
        a = float(input("enter a ="))    
        b = float(input("enter b ="))  
        
        if b == 0:
            result = "Error"

        else :
            result = a / b 

if op == "radical":
        x = float(input("enter x ="))   
        result = math.sqrt(x) 


if op == "sin":
        x = float(input("enter x ="))   
        result = math.sin(x)  

if op == "cos":
        x = float(input("enter x ="))   
        result = math.cos(x) 

if op == "tan":
        x = float(input("enter x ="))   
        result = math.tan(x) 

if op == "cot":
        x = float(input("enter x ="))   
        result = math.cos(x)  / math.sin(x)  

if op == "factorial":
        x = int(input("enter x ="))
        result = math.factorial(x)                           

print (result)