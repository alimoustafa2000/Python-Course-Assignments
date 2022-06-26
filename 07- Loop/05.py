my_numbers = [15, 81, 5, 17, 20, 21, 13]
my_numbers.sort(reverse=True)
a = 1

for num in my_numbers:
    if num % 5 == 0:
        print(f"{a} => {num}")
        a += 1
    else:
        pass

print("All Numbers are Printed")
