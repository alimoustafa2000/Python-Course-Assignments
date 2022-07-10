my_list = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple1 = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_tuple2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data = []

for item1, item2, item3 in zip(my_list, my_tuple1, my_tuple2):

    my_data.append(item1)


my_data.remove(1)
my_data.remove(2)

final_string = "".join(my_data)

print(final_string.lower().capitalize())
# Elzero
