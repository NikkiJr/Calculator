while True:
    try:
        num1 = float(input("Enter a number: "))
        break
    except Exception:
        print('Type a float number!')

op = input("Enter a operator: ") # get the input for operator
while True:
    try:
        num2 = float(input("Enter a number: "))
        break
    except Exception:
        print('Type a float number!')


if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else: 
    print('!!Invaild Operater!!')

