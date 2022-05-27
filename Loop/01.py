User_num = int(input('Enter your number. '))
num = User_num

if num > 0:
    while num > 1:
        num -= 1
        print(num)
    
else:
    print(f"Number {num} isn't larger than 0")


print(f"{User_num - 1} Numbers Printed Successfully.")
