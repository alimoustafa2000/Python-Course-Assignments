def reverse_string(my_string):

    my_reversed_string = list(reversed(my_string))

    string = "".join(my_reversed_string)

    yield string[0]
    yield string[1]
    yield string[2]
    yield string[3]
    yield string[4]
    yield string[5]

myGen = reverse_string('Python')

for character in myGen:

    print(character)



