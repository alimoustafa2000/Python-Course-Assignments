friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

def get_names (name):

    if name[-1] == 'm' :

        return name


# using filter with predefined function 

names = filter(get_names, friends_filter)

for name in names:

    print(name)


# ------------------------------
print("=" * 50)
# ------------------------------


# using filter with lambda function

for name in filter(lambda item: item.endswith("m"), friends_filter):

    print(name)

