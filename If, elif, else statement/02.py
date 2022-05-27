user_age = int(input("What is your age? ").strip())

print("Unfortunately, your age is not suitable for the program" if user_age >= 30 or user_age < 18 else "This program is suitable for you")
