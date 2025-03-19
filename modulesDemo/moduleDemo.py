from customModules import *


n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))
op = input("""
Enter + for Addition
Enter - for Subtraction
Enter * for Multiplication
Enter / for Division
Enter your choice: 
""")
c = calculations.Calculations(n1, n2)

if op=="+":
    print(f"{n1} + {n2} = {c.add()}")
elif op=="-":
    print(f"{n1} - {n2} = {c.sub()}")
elif op=="*":
    print(f"{n1} * {n2} = {c.mult()}")
elif op=="/":
    print(f"{n1} / {n2} = {c.divi()}")
else:
    print("Invalid Operation")