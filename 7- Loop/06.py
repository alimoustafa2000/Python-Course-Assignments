my_numbers = range(1, 21)

for num in my_numbers:
    if num < 10 and num != 6 and num != 8 and num != 12:
        print(str(num).zfill(2))
    elif num == 6 or num == 8 or num == 12:
        continue
    else:
        print(num)

print("All Numbers are Printed")
