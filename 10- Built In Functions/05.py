friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

def remove_chars (text):

    return text[1:-1]


# using map with predefined function 

modified_texts = map(remove_chars, friends_map)

for name in modified_texts:

    print(name)


# ------------------------------
print("=" * 50)
# ------------------------------


# using map with lambda function

for name in map(lambda item: item[1:-1], friends_map):

    print(name)