def calculate (n1, n2, operation):
    if operation == '+' or operation == 'add' or operation == 'a':
        print(int(n1) + int(n2))
    elif operation == '-' or operation == 'subtract' or operation == 's':
        print(int(n1) - int(n2))
    elif operation == '*' or operation == 'multiply' or operation == 'm':
        print(int(n1) * int(n2))
    elif operation == "":
        print(int(n1) + int(n2))
    else:
        print("This Operation Not Available!")

calculate(*input("Enter 2 numbers ").split(), input("Choose the operation [+, -, *] ").lower())