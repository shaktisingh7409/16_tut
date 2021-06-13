print("chose any operator for the list given below\n'+', '-', '*', '/', '**'")
operator = input("Enter the operator: ")
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
total = num1 + operator + num2
if total == "45*3" or total == "3*45":
    print("555")
elif total == "56+9" or total == "9+56":
    print(f"{num1} {operator} {num2} = 77")
elif total == "56/6":
    print("4")
elif operator == "+":
    print(f"{num1} {operator} {num2} = {int(num1) + int(num2)}")
elif operator == "-":
    print(f"{num1} {operator} {num2} = {int(num1) - int(num2)}")
elif operator == "*":
    print(f"{num1} {operator} {num2} = {int(num1) * int(num2)}")
elif operator == "/":
    print(f"{num1} {operator} {num2} = {int(num1) / int(num2)}")
elif operator == "**":
    print(f"{num1} {operator} {num2} = {int(num1) ** int(num2)}")
else:
    print("Can't calculate")
