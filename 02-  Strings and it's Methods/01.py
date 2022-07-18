# ---------------(Assignment 1)---------------

name = "Ali"
age = 22
country = "Egypt"

print(f'Hello {name}, How are you doing? \\""" Your age is "{age}" + Your country is:{country}')

print("="*40)

# ---------------(Assignment 2)---------------

name = "Ali"
age = 22
country = "Egypt"

print(f'Hello {name}, How are you doing? \\\n""" Your age is "{age}" +\nYour country is:{country}')

print("="*40)

# ---------------(Assignment 3)---------------

name = "Abdelkader"


print(f'Second Letter Is "{name[1]}"')
print(f'Third Letter Is "{name[2]}"')
print(f'Last  Letter Is "{name[-1]}"')

print("="*40)

# ---------------(Assignment 4)---------------

name = "Abdelkader"


print(f'Second Letter Is "{name[1:4]}"')
print(f'Third Letter Is "{name[:9:2]}"')

print("="*40)

# ---------------(Assignment 5)---------------

name = "#@#@Ali#@#@"

print(name.strip("#@"))

print("="*40)

# ---------------(Assignment 6)---------------

num1 = "9"
num2 = "15"
num3 = "130"
num4 = "950"
num5 = "1500"

print(num1.zfill(4))
print(num2.zfill(4))
print(num3.zfill(4))
print(num4.zfill(4))
print(num5.zfill(4))

print("="*40)

# ---------------(Assignment 7)---------------

name_one = "Ali"
name_two = "Ali_Moustafa"

print(name_one.rjust(20,"@"))
print(name_two.rjust(20,"@"))

print("="*40)

# ---------------(Assignment 8)---------------

name_one = "MoUstaFa"
name_two = "osaMA"

print(name_one.swapcase())
print(name_two.swapcase())

print("="*40)

# ---------------(Assignment 9)---------------

msg = "I Love Python And, I Love Elzero Web School"

print(msg.count('Love'))

print("="*40)

# ---------------(Assignment 10)---------------

name = "Ali"

print(name.index('i'))

print("="*40)

# ---------------(Assignment 11)---------------

msg = "I Love Python And, I Love Elzero Web School"

print(msg.replace('Love', '<3', 1))

print("="*40)

# ---------------(Assignment 12)---------------

msg = "I <3 Python And Although <3 Elzero Web School"

print(msg.replace('<3', 'Love'))

print("="*40)

# ---------------(Assignment 13)---------------

name = "Ali"
age = 22
country = "Egypt"


print(f"My Name Is {name}, My Age Is {age}, And My Country Is {country}")
