# calc using conditional stt

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation(+, -, *, /, **, %): ")

if op == "+":
    print("sum: ", a+b)
elif op == "-":
    print("Difference: ", a-b)
elif op == "*":
    print("Product: ", a*b)
elif op == "/":
    print("Quotient: ", a/b)
elif op == "**":
    print("Power: ", a**b)
elif op == "%":
    print("Remainder: ", a%b)
else: 
    print("Invalid operation")

