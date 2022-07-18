# ---------------(Assignment 1)---------------

print(bool(True))
print(bool("ali"))
print(bool(100))
print(bool(["ali","ahmed"]))
print(bool(False))
print(bool(0))
print(bool())
print(bool(None))

print("="*40)

# ---------------(Assignment 2)---------------

html = 80
css = 60
javascript = 70

print(html > 50 and css > 50 and javascript > 50 )

print("="*40)

# ---------------(Assignment 3)---------------

num_one = 10
num_two = 20
num = 20

print(num > num_one or num > num_two)

print(num > num_one and num > num_two)

print("="*40)

# ---------------(Assignment 4)---------------

num_one = 10
num_two = 20
result = num_one + num_two

print(result)

Exponent = result ** 3
print(Exponent)

Modulus = Exponent % 26000
print(Modulus)

Division = Modulus / 5
print(Division)

final = str(Division)

print(type(final))
