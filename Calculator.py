num1 = float(input("Enter any number: "))
op = input("Enter an operation:  (+, -, *, /) ")
num2 = float(input("Enter any second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("invalid operation")

