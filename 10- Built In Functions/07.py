nums = [2, 4, 6, 2]

from functools import reduce

def multiply (num1, num2):

    return num1 * num2


# using reduce with predefined function 

result = reduce(multiply, nums)

print(result)


# ------------------------------
print("=" * 50)
# ------------------------------


# using reduce with lambda function

result = reduce(lambda num1, num2: num1 * num2 , nums)

print(result)