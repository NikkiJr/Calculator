while True:
    try:
        num1 = float(input("Enter a number: "))
        break
    except Exception:
        print('type a float number')

op = input("Enter a operator: ") # get the input for operator
num2 = float(input("Enter another number: "))


if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else: #print('Invaild Operater')
    print('Invaild Operater')
#print('This statement is always executed')

# Done!!!.


