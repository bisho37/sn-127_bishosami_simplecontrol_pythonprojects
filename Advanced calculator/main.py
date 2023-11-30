num1 = float(input("enter 1st number:"))
op = input("enter 1st operator:")
num2 = float(input("enter 2nd number:"))
op2 = input("enter 2nd operator:")
num3 = float(input("enter 3rd number:"))

if op == "+" and op2 == "+":
    print(num1 + num2 + num3)
elif op == "+" and op2 == "-":
    print(num1 + num2 - num3)
elif op == "+" and op2 == "*":
    print((num1 + num2) * num3)
elif op == "+" and op2 == "/":
    print((num1 + num2) / num3)
elif op == "-" and op2 == "+":
    print(num1 - num2 + num3)
elif op == "-" and op2 == "-":
    print(num1 - num2 - num3)
elif op == "-" and op2 == "*":
    print((num1 - num2) * num3)
elif op == "-" and op2 == "/":
    print((num1 - num2) / num3)
elif op == "*" and op2 == "+":
    print(num1 * num2 + num3)
elif op == "*" and op2 == "-":
    print(num1 * num2 - num3)
elif op == "*" and op2 == "*":
    print(num1 * num2 * num3)
elif op == "*" and op2 == "/":
    print(num1 * num2 / num3)
elif op == "/" and op2 == "+":
    print(num1 / num2 + num3)
elif op == "/" and op2 == "-":
    print(num1 / num2 - num3)
elif op == "/" and op2 == "*":
    print(num1 / num2 * num3)
elif op == "/" and op2 == "/":
    print(num1 / num2 / num3)
else:
    print("Invalid op or op2")

