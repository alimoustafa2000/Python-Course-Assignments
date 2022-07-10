# --------------------(Method 1)--------------------

def new_member(name = "Unknown", age = "Unknown", country = "Unknown"):

    print(f"Hello {name}, You are from {country} and your age is {age}.")



new_member('Ali', 22, 'Egypt')
# Hello Ali, You are from Egypt and your age is 22.

new_member()
# Hello Unknown, You are from Unknown and your age is Unknown.

print("=" * 40)

# --------------------(Method 2)--------------------

def new_member(name, age, country):

    if name == "":
        name = "Unknown"

    if age == "":
        age = "Unknown"

    if country == "":
        country = "Unknown"

    print(f"Hello {name}, You are from {country} and your age is {age}.")



new_member(input("What's your name? ").capitalize().strip(), input("How old are you? ").capitalize().strip(), input("Where are you from? ").capitalize().strip())