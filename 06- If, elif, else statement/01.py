num1 = int(input("Enter the first number. ").strip())
num2 = int(input("Enter the second number. ").strip())
operation = input('Select the operation: ["+" Or "-" Or "*" Or "/" Or "%"] ').strip()


if operation == '+':
    result = num1  +  num2
    
if operation == '-':
    result = num1  -  num2
    
if operation == '*':
    result = num1  *  num2
    
if operation == '/':
    result = num1  /  num2
    
if operation == '%':
    result = num1  %  num2


print(f"{num1} {operation} {num2} = {result}")
