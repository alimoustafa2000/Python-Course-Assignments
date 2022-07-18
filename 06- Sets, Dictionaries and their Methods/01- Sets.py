# ---------------(Assignment 1)---------------
nums = {1, 2, 3}
letters = {"A", "B", "C"}

print(nums | letters)
print(nums.union(letters))

nums.update(letters)
print(nums)

print("="*40)

# ---------------(Assignment 2)---------------

my_set = {1, 2, 3}

print(my_set)

my_set.clear()
print(my_set)

my_set.add("A")
my_set.add("B")
my_set.discard("C")
print(my_set)

print("="*40)

# ---------------(Assignment 3)---------------

set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}

print(set_one.issubset(set_two))

