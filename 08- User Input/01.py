# ---------------(Assignment 1)---------------

User_name = input("What's your name? ").strip().capitalize()

print(f"Hello {User_name}, Happy To See You Here.")

print("="*40)

# ---------------(Assignment 2)---------------

User_age = int(input("How old are you? ").strip().capitalize())

if User_age < 16 :
    print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")

else:
    print(f"Hello Your Age Is {User_age}, All Articles Is Suitable For You")

print("="*40)

# ---------------(Assignment 3)---------------

First_Name = input("What's your first name? ").strip().capitalize()
Second_Name = input("What's your second name? ").strip().capitalize()

print(f"Hello, {First_Name} {Second_Name[0]}.")

print("="*40)

# ---------------(Assignment 4)---------------

User_email = input("Email Address? ").strip().lower()

print(f"Your username Is {User_email.capitalize()[:User_email.index('@')]}")

print(f"Email Service Provider Is {User_email[User_email.index('@')+1: User_email.index('.')]}")

print(f"Top Level Domain Is {User_email[User_email.index('.')+1:]}")

