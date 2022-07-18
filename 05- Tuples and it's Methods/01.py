# ---------------(Assignment 1)---------------

name = "Ali",

print(name)
print(type(name))

print("="*40)

# ---------------(Assignment 2)---------------

my_friends = ("Osama", "Ahmed", "Sayed")

friends_list = list(my_friends)
friends_list [0] = "Elzero"
friends_tuple = tuple(friends_list)

print(friends_tuple)
print(type(friends_tuple))
print(f"{len(friends_tuple)} Elements")

print("="*40)

# ---------------(Assignment 3)---------------

nums = (1, 2, 3)
letters = ("A", "B", "C")

my_tuple = nums + letters

print(f"my Tuple = {my_tuple}")
print(f"{len(my_tuple)} Elements")

print("="*40)

# ---------------(Assignment 4)---------------

my_tuple = (1, 2, 3, 4)

A,B,_,C = my_tuple

print(A)
print(B)
print(C)



