my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []

for data in zip(my_list, my_tuple):

    a = list(data)

    x = "".join(a)

    my_data.append(x)


final_string = "".join(my_data)

print(final_string.lower().capitalize())
# Elzero